---
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/models.py#LyricsDocument
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/search.py#LyricsSearchResult
---

# Lyrics

One complete timed lyric document, whether found in a search or selected for the active song. Display-only text conversion does not alter its source text.

## Information kept

- **Provider** — The source that produced the lyric content.
- **Song identity** — The provider song identity when available.
- **Metadata** — The lyric title, artist, album, and duration.
- **Timed text** — Ordered lines and optional word timing, with available translations.
- **Timing** — Line or word timing.
- **Confidence** — The match quality for the searched or resolved recording.
- **Acquisition** — Network, cache, live, sidecar, embedded, adapter, or manual acquisition.
- **Cache state** — No cache, automatic cache, or manual selection as reported for the active document.
