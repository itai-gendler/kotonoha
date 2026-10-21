---
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.select
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#_selection_key
---

# Manual selection

The listener’s lasting choice of lyric content for a playback recording. It remains independent of edited search terms and provider metadata.

## Information kept

- **Playback identity** — The original playback title and artist plus duration rounded to a tenth of a second; album is excluded.
- **Chosen lyrics** — The provider and song identity selected for that playback identity.
