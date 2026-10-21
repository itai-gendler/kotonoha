---
appliesTo:
- type: entity
  id: cached-lyrics
  effect: removes
permits:
- actors:
  - listener
- unattended: true
references:
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage
---

# Cached lyrics are removed by the listener or by Kotonoha's automatic cleanup

The listener deletes selected entries or clears the cache after confirming. Kotonoha itself removes the oldest automatic entries beyond the cache limit and content that no longer yields timed lyrics.
