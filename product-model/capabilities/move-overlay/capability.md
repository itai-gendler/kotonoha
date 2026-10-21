---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: README.md
- kind: doc
  role: intent
  target: docs/SPEC.md
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/window.py#LyricsOverlay.mousePressEvent
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/position.py#OverlayPositionController.commit_drag_position
domain: position
---

# Move the overlay

Reposition an unlocked overlay using the movement supported by the desktop platform.
