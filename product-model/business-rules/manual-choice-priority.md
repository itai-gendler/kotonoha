---
appliesTo:
- type: entity
  id: manual-selection
- type: entity
  id: lyrics
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver._lookup_manual
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.lookup_manual
---

# A saved manual choice precedes automatic lyric sources

With cache restoration enabled, a playback binding is checked before exact hints and normal source plans. A bound choice is user-confirmed and does not need to pass automatic matching again.
