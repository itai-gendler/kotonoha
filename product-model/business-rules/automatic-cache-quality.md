---
appliesTo:
- type: entity
  id: cached-lyrics
- type: entity
  id: lyrics
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/__init__.py#LyricsCache.store
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.lookup
---

# Automatic cache content requires a high-confidence timed result

Only high-confidence automatic results are saved. An automatic cache entry is used only by the provider it came from. Lyrics read from local files or received from live sources are not cached.
