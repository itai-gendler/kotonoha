---
appliesTo:
- type: entity
  id: manual-selection
- type: entity
  id: cached-lyrics
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage._write
- kind: code
  role: implementation
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController._apply_async
---

# Manual content and its playback binding are saved together

Applying a result commits cached content and its binding atomically before attempting immediate display replacement. A failed save is not reported as a successful selection.
