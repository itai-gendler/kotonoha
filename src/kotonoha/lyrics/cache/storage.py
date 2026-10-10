"""Synchronous SQLite storage for the lyrics cache facade."""

from __future__ import annotations

import json
import math
import os
import sqlite3
import time
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Final

from ..artifact import LyricsArtifact
from ..match import Candidate, MatchConfidence, MatchEvidence, TrackMetadata, evaluate_match
from ..models import LyricLine
from ..title_grammar import NORMALIZER_VERSION
from .models import (
    CacheDeleteResult,
    CacheDeleteStatus,
    CacheWriteResult,
    CacheWriteStatus,
    LyricsCacheEntry,
    LyricsCacheHit,
    LyricsCacheKey,
    LyricsCacheMode,
    LyricsCacheQuery,
)

CACHE_SCHEMA_VERSION = 1
DEFAULT_MAX_ENTRIES = 1000
_CACHE_SEARCH_FIELDS: Final[tuple[str, ...]] = ("title", "artist", "album", "provider", "provider_song_id")

PayloadParser = Callable[[Mapping[str, str]], tuple[LyricLine, ...]]

_SCHEMA = """
CREATE TABLE IF NOT EXISTS lyrics (
    provider TEXT NOT NULL,
    provider_song_id TEXT NOT NULL,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    album TEXT NOT NULL,
    mode TEXT NOT NULL DEFAULT 'auto',
    selection_only INTEGER NOT NULL DEFAULT 0,
    duration_s REAL,
    payload_json TEXT NOT NULL,
    fetched_at REAL NOT NULL,
    last_accessed REAL NOT NULL,
    schema_version INTEGER NOT NULL,
    normalizer_version INTEGER NOT NULL,
    PRIMARY KEY (provider, provider_song_id)
);
CREATE INDEX IF NOT EXISTS lyrics_provider_access
    ON lyrics(provider, last_accessed DESC);
CREATE TABLE IF NOT EXISTS lyric_selections (
    track_key TEXT PRIMARY KEY,
    provider TEXT NOT NULL,
    provider_song_id TEXT NOT NULL,
    FOREIGN KEY (provider, provider_song_id)
        REFERENCES lyrics(provider, provider_song_id) ON DELETE CASCADE
);
"""


def cache_path() -> Path:
    """Return the XDG cache path used by the application by default."""
    base = os.environ.get("XDG_CACHE_HOME") or os.path.join(os.path.expanduser("~"), ".cache")
    return Path(base) / "kotonoha" / "lyrics.sqlite3"


class LyricsCacheStorage:
    """Own synchronous SQLite operations for one validated cache database."""

    def __init__(self, path: Path, *, max_entries: int) -> None:
        """Create a storage owner without opening a database connection."""
        self._path = path
        self._max_entries = max(1, max_entries)

    def lookup(self, provider: str, track: TrackMetadata, parser: PayloadParser) -> LyricsCacheHit | None:
        """Return one high-confidence automatic hit for a provider."""
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT * FROM lyrics "
                "WHERE provider = ? AND mode = ? AND schema_version = ? AND normalizer_version = ?",
                (provider, LyricsCacheMode.AUTO.value, CACHE_SCHEMA_VERSION, NORMALIZER_VERSION),
            ).fetchall()
            matches: list[tuple[MatchEvidence, sqlite3.Row]] = []
            for row in rows:
                evidence = self._match_row(row, track)
                if evidence.confidence is MatchConfidence.HIGH:
                    matches.append((evidence, row))
            matches.sort(key=lambda item: self._match_sort_key(item[0]), reverse=True)
            for evidence, row in matches:
                hit = self._read_hit(connection, row, evidence.confidence, parser, LyricsCacheMode.AUTO)
                if hit is not None:
                    return hit
            return None

    def lookup_manual(
        self,
        track: TrackMetadata,
        parsers: Mapping[str, PayloadParser],
    ) -> LyricsCacheHit | None:
        """Restore a playback binding first, then match unbound legacy manual rows."""
        with self._connect() as connection:
            selection_key = _selection_key(track)
            selected = connection.execute(
                "SELECT lyrics.* FROM lyric_selections JOIN lyrics USING (provider, provider_song_id) "
                "WHERE track_key IN (?, ?) AND schema_version = ? AND normalizer_version = ? "
                "ORDER BY track_key = ? DESC",
                (selection_key, _legacy_selection_key(track), CACHE_SCHEMA_VERSION, NORMALIZER_VERSION, selection_key),
            ).fetchone()
            if selected is not None:
                parser = parsers.get(selected["provider"])
                if parser is None:
                    return None
                return self._read_hit(
                    connection, selected, MatchConfidence.HIGH, parser, LyricsCacheMode.MANUAL,
                )
            # TODO: Remove heuristic restoration when unbound legacy MANUAL rows have
            # been deleted or reselected; their original playback identity was not stored.
            rows = connection.execute(
                "SELECT * FROM lyrics "
                "WHERE mode = ? AND schema_version = ? AND normalizer_version = ? AND selection_only = 0 "
                "ORDER BY last_accessed DESC, provider ASC, provider_song_id ASC",
                (LyricsCacheMode.MANUAL.value, CACHE_SCHEMA_VERSION, NORMALIZER_VERSION),
            ).fetchall()
            matches: list[tuple[MatchEvidence, sqlite3.Row, PayloadParser]] = []
            for row in rows:
                parser = parsers.get(row["provider"])
                if parser is None:
                    continue
                evidence = self._match_row(row, track)
                if evidence.confidence is not MatchConfidence.NONE:
                    matches.append((evidence, row, parser))

            matches.sort(key=lambda item: self._manual_sort_key(item[0], item[1]), reverse=True)
            for evidence, row, parser in matches:
                hit = self._read_hit(connection, row, evidence.confidence, parser, LyricsCacheMode.MANUAL)
                if hit is not None:
                    return hit
            return None

    def search(self, query: LyricsCacheQuery) -> tuple[LyricsCacheEntry, ...]:
        """Return cache metadata in deterministic recent-use order."""
        keyword = query.keyword.strip().casefold()
        with self._connect() as connection:
            if query.provider is None:
                rows = connection.execute(
                    "SELECT provider, provider_song_id, title, artist, album, mode, duration_s, fetched_at, "
                    "last_accessed FROM lyrics ORDER BY last_accessed DESC, provider ASC, provider_song_id ASC"
                ).fetchall()
            else:
                rows = connection.execute(
                    "SELECT provider, provider_song_id, title, artist, album, mode, duration_s, fetched_at, "
                    "last_accessed FROM lyrics WHERE provider = ? "
                    "ORDER BY last_accessed DESC, provider ASC, provider_song_id ASC",
                    (query.provider,),
                ).fetchall()
        entries = tuple(self._entry_from_row(row) for row in rows)
        if not keyword:
            return entries
        return tuple(entry for entry in entries if _entry_matches(entry, keyword))

    def get(self, key: LyricsCacheKey) -> LyricsCacheEntry | None:
        """Return one cache entry by its provider-scoped key."""
        with self._connect() as connection:
            row = connection.execute(
                "SELECT provider, provider_song_id, title, artist, album, mode, duration_s, fetched_at, last_accessed "
                "FROM lyrics WHERE provider = ? AND provider_song_id = ?",
                (key.provider, key.provider_song_id),
            ).fetchone()
        return None if row is None else self._entry_from_row(row)

    def upsert(self, artifact: LyricsArtifact, mode: LyricsCacheMode) -> CacheWriteResult:
        """Create or replace one validated artifact and prune oldest rows."""
        return self._write(artifact, mode, None)

    def select(self, track: TrackMetadata, artifact: LyricsArtifact) -> CacheWriteResult:
        """Atomically persist the artifact and replace this playback track's choice."""
        return self._write(artifact, LyricsCacheMode.MANUAL, _selection_key(track))

    def _write(
        self, artifact: LyricsArtifact, mode: LyricsCacheMode, track_key: str | None,
    ) -> CacheWriteResult:
        """Keep content, selection replacement, and eviction in one transaction.

        The permanent selection_only marker prevents superseded bound content
        from being mistaken for a legacy manual choice after its binding changes.
        """
        now = time.time()
        payload_json = json.dumps(artifact.payload, ensure_ascii=False, separators=(",", ":"))
        key = LyricsCacheKey(artifact.provider, artifact.provider_song_id)
        with self._connect() as connection:
            existed = connection.execute(
                "SELECT 1 FROM lyrics WHERE provider = ? AND provider_song_id = ?",
                (key.provider, key.provider_song_id),
            ).fetchone() is not None
            connection.execute(
                "INSERT INTO lyrics ("
                "provider, provider_song_id, title, artist, album, mode, duration_s, payload_json, "
                "fetched_at, last_accessed, schema_version, normalizer_version, selection_only"
                ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
                "ON CONFLICT(provider, provider_song_id) DO UPDATE SET "
                "title = excluded.title, artist = excluded.artist, album = excluded.album, mode = excluded.mode, "
                "duration_s = excluded.duration_s, payload_json = excluded.payload_json, "
                "fetched_at = excluded.fetched_at, last_accessed = excluded.last_accessed, "
                "schema_version = excluded.schema_version, normalizer_version = excluded.normalizer_version, "
                "selection_only = MAX(lyrics.selection_only, excluded.selection_only)",
                (
                    artifact.provider,
                    artifact.provider_song_id,
                    artifact.title,
                    artifact.artist,
                    artifact.album,
                    mode.value,
                    artifact.duration_s,
                    payload_json,
                    now,
                    now,
                    CACHE_SCHEMA_VERSION,
                    NORMALIZER_VERSION,
                    int(track_key is not None),
                ),
            )
            if track_key is not None:
                connection.execute(
                    "INSERT INTO lyric_selections (track_key, provider, provider_song_id) VALUES (?, ?, ?) "
                    "ON CONFLICT(track_key) DO UPDATE SET provider = excluded.provider, "
                    "provider_song_id = excluded.provider_song_id",
                    (track_key, artifact.provider, artifact.provider_song_id),
                )
            connection.execute(
                "DELETE FROM lyrics WHERE selection_only = 0 AND mode = ? AND rowid IN ("
                "SELECT rowid FROM lyrics WHERE selection_only = 0 AND mode = ? "
                "ORDER BY last_accessed DESC LIMIT -1 OFFSET ?)",
                (LyricsCacheMode.AUTO.value, LyricsCacheMode.AUTO.value, self._max_entries),
            )
        status = CacheWriteStatus.UPDATED if existed else CacheWriteStatus.CREATED
        return CacheWriteResult(key, status)

    def update(self, key: LyricsCacheKey, artifact: LyricsArtifact, mode: LyricsCacheMode) -> CacheWriteResult:
        """Update one existing artifact and preserve its provider-scoped identity."""
        now = time.time()
        payload_json = json.dumps(artifact.payload, ensure_ascii=False, separators=(",", ":"))
        with self._connect() as connection:
            cursor = connection.execute(
                "UPDATE lyrics SET title = ?, artist = ?, album = ?, mode = ?, duration_s = ?, payload_json = ?, "
                "fetched_at = ?, last_accessed = ?, schema_version = ?, normalizer_version = ? "
                "WHERE provider = ? AND provider_song_id = ?",
                (
                    artifact.title,
                    artifact.artist,
                    artifact.album,
                    mode.value,
                    artifact.duration_s,
                    payload_json,
                    now,
                    now,
                    CACHE_SCHEMA_VERSION,
                    NORMALIZER_VERSION,
                    key.provider,
                    key.provider_song_id,
                ),
            )
        status = CacheWriteStatus.UPDATED if cursor.rowcount else CacheWriteStatus.NOT_FOUND
        return CacheWriteResult(key, status)

    def delete(self, key: LyricsCacheKey) -> CacheDeleteResult:
        """Delete one cache entry and report whether it existed."""
        with self._connect() as connection:
            cursor = connection.execute(
                "DELETE FROM lyrics WHERE provider = ? AND provider_song_id = ?",
                (key.provider, key.provider_song_id),
            )
        status = CacheDeleteStatus.DELETED if cursor.rowcount else CacheDeleteStatus.NOT_FOUND
        return CacheDeleteResult(key, status)

    def delete_many(self, keys: tuple[LyricsCacheKey, ...]) -> tuple[CacheDeleteResult, ...]:
        """Delete several exact entries in one SQLite transaction."""
        with self._connect() as connection:
            results: list[CacheDeleteResult] = []
            for key in keys:
                cursor = connection.execute(
                    "DELETE FROM lyrics WHERE provider = ? AND provider_song_id = ?",
                    (key.provider, key.provider_song_id),
                )
                status = CacheDeleteStatus.DELETED if cursor.rowcount else CacheDeleteStatus.NOT_FOUND
                results.append(CacheDeleteResult(key, status))
        return tuple(results)

    def clear(self) -> None:
        """Delete every persisted lyric cache entry."""
        with self._connect() as connection:
            connection.execute("DELETE FROM lyrics")

    def count(self) -> int:
        """Return the number of persisted lyric cache entries."""
        with self._connect() as connection:
            row = connection.execute("SELECT COUNT(*) AS count FROM lyrics").fetchone()
        return int(row["count"]) if row is not None else 0

    def _connect(self) -> sqlite3.Connection:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self._path, timeout=3.0)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript(_SCHEMA)
        self._ensure_columns(connection)
        return connection

    @staticmethod
    def _ensure_columns(connection: sqlite3.Connection) -> None:
        """Add metadata introduced after the first cache schema without losing rows."""
        columns = {row["name"] for row in connection.execute("PRAGMA table_info(lyrics)")}
        if "mode" not in columns:
            connection.execute("ALTER TABLE lyrics ADD COLUMN mode TEXT NOT NULL DEFAULT 'auto'")
        if "selection_only" not in columns:
            connection.execute("ALTER TABLE lyrics ADD COLUMN selection_only INTEGER NOT NULL DEFAULT 0")

    @staticmethod
    def _match_row(row: sqlite3.Row, track: TrackMetadata) -> MatchEvidence:
        """Build match evidence from one validated cache metadata row."""
        candidate = Candidate(
            song_id=row["provider_song_id"],
            title=row["title"],
            artist=row["artist"],
            duration_s=row["duration_s"],
            album=row["album"],
        )
        return evaluate_match(candidate, track)

    def _read_hit(
        self,
        connection: sqlite3.Connection,
        row: sqlite3.Row,
        confidence: MatchConfidence,
        parser: PayloadParser,
        mode: LyricsCacheMode,
    ) -> LyricsCacheHit | None:
        """Parse one selected row and remove it when its payload is invalid."""
        provider = row["provider"]
        try:
            raw_payload = json.loads(row["payload_json"])
            if not isinstance(raw_payload, dict) or not all(
                isinstance(key, str) and isinstance(value, str) for key, value in raw_payload.items()
            ):
                raise TypeError("cached payload is not a string map")
            payload: dict[str, str] = raw_payload
            lines = parser(payload)
            if not lines:
                raise ValueError("cached payload has no timed lyrics")
        except (json.JSONDecodeError, TypeError, ValueError):
            connection.execute(
                "DELETE FROM lyrics WHERE provider = ? AND provider_song_id = ?",
                (provider, row["provider_song_id"]),
            )
            return None

        connection.execute(
            "UPDATE lyrics SET last_accessed = ? WHERE provider = ? AND provider_song_id = ?",
            (time.time(), provider, row["provider_song_id"]),
        )
        return LyricsCacheHit(
            artifact=LyricsArtifact(
                provider=provider,
                provider_song_id=row["provider_song_id"],
                title=row["title"],
                artist=row["artist"],
                album=row["album"],
                duration_s=row["duration_s"],
                payload=payload,
                lines=lines,
                confidence=confidence,
            ),
            mode=mode,
        )

    @staticmethod
    def _match_sort_key(evidence: MatchEvidence) -> tuple[bool, bool, bool, float]:
        duration_rank = -evidence.duration_delta if evidence.duration_delta is not None else float("-inf")
        return evidence.title_exact, evidence.artist_overlap, evidence.album_match, duration_rank

    @staticmethod
    def _manual_sort_key(evidence: MatchEvidence, row: sqlite3.Row) -> tuple[int, bool, bool, bool, float, float]:
        confidence_rank = {
            MatchConfidence.NONE: 0,
            MatchConfidence.MEDIUM: 1,
            MatchConfidence.HIGH: 2,
        }
        duration_rank = -evidence.duration_delta if evidence.duration_delta is not None else float("-inf")
        last_accessed = row["last_accessed"]
        return (
            confidence_rank[evidence.confidence],
            evidence.title_exact,
            evidence.artist_overlap,
            evidence.album_match,
            duration_rank,
            float(last_accessed) if isinstance(last_accessed, (int, float)) else float("-inf"),
        )

    @staticmethod
    def _entry_from_row(row: sqlite3.Row) -> LyricsCacheEntry:
        """Validate one SQLite metadata row before exposing it to the application."""
        provider = row["provider"]
        provider_song_id = row["provider_song_id"]
        title = row["title"]
        artist = row["artist"]
        album = row["album"]
        raw_mode = row["mode"]
        duration = row["duration_s"]
        fetched_at = row["fetched_at"]
        last_accessed = row["last_accessed"]
        if not all(isinstance(value, str) for value in (provider, provider_song_id, title, artist, album, raw_mode)):
            raise TypeError("cache metadata contains a non-string value")
        try:
            mode = LyricsCacheMode(raw_mode)
        except ValueError as exc:
            raise ValueError("cache mode is invalid") from exc
        if duration is not None and (not isinstance(duration, (int, float)) or isinstance(duration, bool)):
            raise TypeError("cache duration is not numeric")
        if not isinstance(fetched_at, (int, float)) or isinstance(fetched_at, bool):
            raise TypeError("cache fetch time is not numeric")
        if not isinstance(last_accessed, (int, float)) or isinstance(last_accessed, bool):
            raise TypeError("cache access time is not numeric")
        return LyricsCacheEntry(
            key=LyricsCacheKey(provider, provider_song_id),
            title=title,
            artist=artist,
            album=album,
            duration_s=float(duration) if duration is not None else None,
            fetched_at=float(fetched_at),
            last_accessed=float(last_accessed),
            mode=mode,
        )


def _selection_key(track: TrackMetadata) -> str:
    """Serialize title, artist, and rounded duration as the playback identity.

    Album metadata is deliberately excluded because players frequently omit or alter
    it while the same track remains active.
    """
    if not all(isinstance(value, str) for value in (track.title, track.artist, track.album)):
        raise TypeError("selection metadata must contain strings")
    duration = track.duration_s
    if duration is not None and (not math.isfinite(duration) or duration < 0):
        raise ValueError("selection duration must be finite and nonnegative")
    normalized_duration = None if duration is None else float(round(duration, 1))
    return json.dumps(
        (track.title, track.artist, normalized_duration),
        ensure_ascii=False, separators=(",", ":"),
    )


def _legacy_selection_key(track: TrackMetadata) -> str:
    """Return the pre-album-removal key for one-time compatibility lookup."""
    duration = track.duration_s
    normalized_duration = None if duration is None else float(round(duration, 1))
    return json.dumps(
        (track.title, track.artist, track.album, normalized_duration),
        ensure_ascii=False, separators=(",", ":"),
    )


def _entry_matches(entry: LyricsCacheEntry, keyword: str) -> bool:
    """Match a case-folded keyword against all searchable cache metadata."""
    values = {
        "title": entry.title,
        "artist": entry.artist,
        "album": entry.album,
        "provider": entry.key.provider,
        "provider_song_id": entry.key.provider_song_id,
    }
    return any(keyword in values[field].casefold() for field in _CACHE_SEARCH_FIELDS)


__all__ = [
    "CACHE_SCHEMA_VERSION",
    "DEFAULT_MAX_ENTRIES",
    "LyricsCacheStorage",
    "PayloadParser",
    "cache_path",
]
