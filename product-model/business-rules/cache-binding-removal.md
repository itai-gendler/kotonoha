---
appliesTo:
- type: entity
  id: cached-lyrics
  effect: removes
- type: entity
  id: manual-selection
- type: entity
  id: timing-correction
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py
- kind: code
  role: implementation
  target: src/kotonoha/state/track_offset_store.py#TrackOffsetStore
---

# Removing cached content also removes its manual bindings

Deleting, clearing, or discarding corrupt content removes every binding referring to it. Saved timing corrections are kept separately and survive these cache operations.
