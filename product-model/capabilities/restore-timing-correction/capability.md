---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: docs/SPEC.md
- kind: code
  role: implementation
  target: src/kotonoha/state/track_offset_store.py#TrackOffsetStore.load
- kind: code
  role: implementation
  target: src/kotonoha/display/presentation.py#DisplayEngine._display_position
---

# Restore a timing correction

Reuse the saved correction for the displayed recording and exact lyric version after a return to the song or application restart.
