---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/__init__.py#LyricsCache.store
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver
domain: sources
---

# Cache lyrics

Retain high-confidence automatic network results for later reuse when caching is enabled. Explicit manual application uses its own save path.
