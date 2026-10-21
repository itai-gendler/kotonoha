---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: docs/SPEC.md
- kind: code
  role: implementation
  target: src/kotonoha/providers/player_selection.py#PlayerSelector.choose
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_playback.py#MprisPlaybackCoordinator
- kind: code
  role: implementation
  target: src/kotonoha/app/source_gate.py#SourceOwnershipCoordinator
domain: sources
---

# Follow a player

Automatically follow eligible playback using the preferred-player setting and the shared selection policy.
