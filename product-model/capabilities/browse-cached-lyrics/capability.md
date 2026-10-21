---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: README.md
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.search
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheTableModel
domain: local-lyrics-cache
---

# Browse cached lyrics

Search stored metadata by title, artist, album, provider, or provider song identity, in recent-use order.
