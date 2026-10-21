---
appliesTo:
- type: entity
  id: lyrics
- type: entity
  id: settings
  facts:
  - Lyric sources
  - Prefer best match
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver
---

# Match confidence and source order determine automatic selection

Best-match mode ranks confidence first and configured order breaks ties. Ordered mode chooses the first valid result, checking each provider’s cache at its own place. Manual restoration precedes both policies. Failures are distinct from negative results.
