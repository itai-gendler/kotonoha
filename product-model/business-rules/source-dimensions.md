---
appliesTo:
- type: entity
  id: settings
  facts:
  - Display sources
  - Lyric sources
- type: entity
  id: track
- type: entity
  id: lyrics
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: doc
  role: intent
  target: docs/SPEC.md
- kind: code
  role: implementation
  target: src/kotonoha/app/services.py#RuntimeConfigApplier.apply
- kind: code
  role: implementation
  target: src/kotonoha/app/source_gate.py#SourceOwnershipCoordinator
- kind: code
  role: implementation
  target: src/kotonoha/app/display_coordinator.py#DisplayCoordinator.current_lyrics_status
---

# Playback source and lyric provider remain independent

Display sources choose which source supplies playback and live lyrics. Lyric sources choose lookup order. The status view separately reports provider, acquisition, playback source, and cache state. Enabling Cider as a lyric source enables its probing; it is disabled by default.
