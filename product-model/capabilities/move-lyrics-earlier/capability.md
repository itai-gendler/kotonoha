---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: docs/SPEC.md
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/content.py#OverlayContentController
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController._handle_intent
- kind: code
  role: implementation
  target: src/kotonoha/app/track_offset_service.py#TrackOffsetService
---

# Move lyrics earlier

Adjust the current recording’s exact lyric timeline earlier by 100 milliseconds and persist the correction.
