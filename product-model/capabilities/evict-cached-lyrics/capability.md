---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage._write
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage._read_hit
domain: sources
---

# Evict cached lyrics

Remove old automatic content to enforce cache capacity, and discard content that cannot be restored as timed lyrics.
