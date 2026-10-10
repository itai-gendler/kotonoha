"""Persistent manual choices belong to playback metadata, not provider matches."""

import sqlite3
from pathlib import Path

import pytest

from kotonoha.async_worker import BlockingCallRunner
from kotonoha.lyrics import netease
from kotonoha.lyrics.artifact import LyricsArtifact
from kotonoha.lyrics.cache import LyricsCache, LyricsCacheError, LyricsCacheKey, LyricsCacheMode
from kotonoha.lyrics.match import MatchConfidence, TrackMetadata
from kotonoha.lyrics.models import LyricLine


def make_cache(path: Path, *, max_entries: int = 1000) -> LyricsCache:
    return LyricsCache(path, worker=BlockingCallRunner("test-selections"), max_entries=max_entries)


def candidate(song_id: str) -> LyricsArtifact:
    return LyricsArtifact(
        "netease", song_id, "Provider title", "Provider artist", "Provider album", 180.0,
        {"lrc": f"[00:01.00]{song_id}"},
        (LyricLine(0, "L0", 1.0, 6.0, song_id, ""),), MatchConfidence.HIGH,
    )


async def test_selection_survives_reopening_and_automatic_writes(tmp_path: Path) -> None:
    path = tmp_path / "lyrics.sqlite3"
    track = TrackMetadata("Playback title (Live)", "Uploader", "Playback album", 200.0)
    cache = make_cache(path)
    try:
        await cache.select(track, candidate("chosen"))
        await cache.store(candidate("chosen"))
    finally:
        cache.close()
    reopened = make_cache(path)
    try:
        hit = await reopened.lookup_manual(track, {"netease": netease.parse_payload})
        assert hit is not None
        assert hit.mode is LyricsCacheMode.MANUAL
        assert hit.artifact.provider_song_id == "chosen"
        assert hit.artifact.lines[0].text == "chosen"
        assert hit.artifact.confidence is MatchConfidence.HIGH
    finally:
        reopened.close()


async def test_last_choice_replaces_only_its_playback_track(tmp_path: Path) -> None:
    cache = make_cache(tmp_path / "lyrics.sqlite3")
    first = TrackMetadata("Song", "Artist", "Album", 180.0)
    second = TrackMetadata("Song (Live)", "Artist", "Album", 180.0)
    try:
        await cache.select(first, candidate("old"))
        await cache.select(second, candidate("old"))
        await cache.select(first, candidate("new"))
        for track, song_id in ((first, "new"), (second, "old")):
            hit = await cache.lookup_manual(track, {"netease": netease.parse_payload})
            assert hit is not None and hit.artifact.provider_song_id == song_id
        assert await cache.lookup_manual(
            TrackMetadata("Provider title", "Provider artist", "Provider album", 180.0),
            {"netease": netease.parse_payload},
        ) is None
    finally:
        cache.close()


async def test_album_changes_do_not_change_manual_selection_identity(tmp_path: Path) -> None:
    cache = make_cache(tmp_path / "lyrics.sqlite3")
    try:
        await cache.select(TrackMetadata("Song", "Artist", "Album A", 180.0), candidate("chosen"))
        hit = await cache.lookup_manual(
            TrackMetadata("Song", "Artist", "Album B", 180.0),
            {"netease": netease.parse_payload},
        )
        assert hit is not None and hit.artifact.provider_song_id == "chosen"
    finally:
        cache.close()


async def test_manual_entries_are_exempt_from_lru_eviction(tmp_path: Path) -> None:
    cache = make_cache(tmp_path / "lyrics.sqlite3", max_entries=1)
    track = TrackMetadata("Playback title", "Uploader")
    try:
        await cache.select(track, candidate("chosen"))
        await cache.store(candidate("automatic"))
        await cache.store(candidate("newest"))
        hit = await cache.lookup_manual(track, {"netease": netease.parse_payload})
        assert hit is not None and hit.artifact.provider_song_id == "chosen"
    finally:
        cache.close()


async def test_replaced_choice_does_not_become_a_legacy_metadata_match(tmp_path: Path) -> None:
    cache = make_cache(tmp_path / "lyrics.sqlite3")
    track = TrackMetadata("Playback title", "Uploader")
    try:
        await cache.select(track, candidate("old"))
        await cache.select(track, candidate("new"))
        await cache.delete(LyricsCacheKey("netease", "new"))
        assert await cache.lookup_manual(
            TrackMetadata("Provider title", "Provider artist", "Provider album", 180.0),
            {"netease": netease.parse_payload},
        ) is None
    finally:
        cache.close()


async def test_binding_failure_rolls_back_content_and_preserves_previous_choice(tmp_path: Path) -> None:
    path = tmp_path / "lyrics.sqlite3"
    cache = make_cache(path)
    track = TrackMetadata("Playback title", "Uploader")
    try:
        await cache.select(track, candidate("old"))
        with sqlite3.connect(path) as connection:
            connection.execute(
                "CREATE TRIGGER reject_selection BEFORE UPDATE ON lyric_selections "
                "BEGIN SELECT RAISE(ABORT, 'test selection failure'); END"
            )
        with pytest.raises(LyricsCacheError):
            await cache.select(track, candidate("new"))
        hit = await cache.lookup_manual(track, {"netease": netease.parse_payload})
        assert hit is not None and hit.artifact.provider_song_id == "old"
        assert await cache.get(LyricsCacheKey("netease", "new")) is None
    finally:
        cache.close()


@pytest.mark.parametrize("cleanup", ["delete", "delete_many", "clear", "corrupt"])
async def test_removed_artifact_cannot_restore_a_stale_selection(tmp_path: Path, cleanup: str) -> None:
    cache = make_cache(tmp_path / "lyrics.sqlite3", max_entries=1)
    track = TrackMetadata("Playback title", "Uploader")
    try:
        await cache.select(track, candidate("chosen"))
        key = LyricsCacheKey("netease", "chosen")
        if cleanup == "delete":
            await cache.delete(key)
        elif cleanup == "delete_many":
            await cache.delete_many((key,))
        elif cleanup == "clear":
            await cache.clear()
        elif cleanup == "corrupt":
            with sqlite3.connect(tmp_path / "lyrics.sqlite3") as connection:
                connection.execute("UPDATE lyrics SET payload_json = ?", ("invalid json",))
            assert await cache.lookup_manual(track, {"netease": netease.parse_payload}) is None
        else:
            await cache.store(candidate("other"))
        await cache.store(candidate("chosen"))
        assert await cache.lookup_manual(track, {"netease": netease.parse_payload}) is None
    finally:
        cache.close()


async def test_unavailable_parser_does_not_erase_a_saved_choice(tmp_path: Path) -> None:
    cache = make_cache(tmp_path / "lyrics.sqlite3")
    track = TrackMetadata("Playback title", "Uploader")
    try:
        await cache.select(track, candidate("chosen"))
        assert await cache.lookup_manual(track, {}) is None
        hit = await cache.lookup_manual(track, {"netease": netease.parse_payload})
        assert hit is not None and hit.artifact.provider_song_id == "chosen"
    finally:
        cache.close()


@pytest.mark.parametrize("selected_duration, restored_duration", [(180, 180.0), (180.0, 180)])
async def test_equal_numeric_durations_restore_the_same_selection(
    tmp_path: Path, selected_duration: float, restored_duration: float,
) -> None:
    """Integer and floating-point durations identify the same playback track."""
    cache = make_cache(tmp_path / "lyrics.sqlite3")
    try:
        await cache.select(
            TrackMetadata("Playback title", "Uploader", duration_s=selected_duration),
            candidate("chosen"),
        )
        hit = await cache.lookup_manual(
            TrackMetadata("Playback title", "Uploader", duration_s=restored_duration),
            {"netease": netease.parse_payload},
        )
        assert hit is not None and hit.artifact.provider_song_id == "chosen"
    finally:
        cache.close()
