---
appliesTo:
- type: entity
  id: settings
  facts:
  - Placement
references:
- kind: doc
  role: intent
  target: docs/SPEC.md
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/drag.py#OverlayDragController.end
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/position.py#OverlayPositionController.commit_drag_position
---

# Saved placement reflects a successfully applied move

Manual placement is saved only when the platform accepts the movement and supports reliable client positioning. Rebinding to another output must succeed before its placement is committed. Ordinary Wayland system movement stays compositor-owned.
