---
appliesTo:
- type: entity
  id: cached-lyrics
- type: entity
  id: manual-selection
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage._write
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.lookup_manual
---

# Automatic eviction preserves manually selected content

The automatic recency limit applies to ordinary AUTO records. Manual records and content ever bound to an explicit playback choice are exempt. Replacing a binding does not turn its old content into an unbound legacy manual match.
