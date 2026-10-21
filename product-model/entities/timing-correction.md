---
references:
- kind: doc
  role: intent
  target: docs/SPEC.md
- kind: code
  role: implementation
  target: src/kotonoha/display/offsets.py#track_offset_key
- kind: code
  role: implementation
  target: src/kotonoha/state/track_offset_store.py#TrackOffsetStore
---

# Timing correction

A saved adjustment for one recording and one exact lyric version. Cache deletion does not remove these separately stored corrections.

## Information kept

- **Recording** — Normalized title, artist, album, and whole-second duration.
- **Lyric version** — The provider, song identity, and exact source lyric content, including timing and translations.
- **Correction** — A signed timing correction in milliseconds, separate from the global lead.
