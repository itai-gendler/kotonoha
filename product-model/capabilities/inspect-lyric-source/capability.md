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
  target: src/kotonoha/app/display_coordinator.py#DisplayCoordinator.current_lyrics_status
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_status.py
---

# Inspect the lyric source

Read the active lyric provider, acquisition method, playback source, and cache state independently.
