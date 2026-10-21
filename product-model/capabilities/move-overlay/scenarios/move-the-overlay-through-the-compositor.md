---
kind: alternate
routes:
  main: Main
steps:
- text: The listener starts an overlay move.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::overlay
- text: The Product asks the compositor to perform the move.
  kind: product
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/window.py#LyricsOverlay.mousePressEvent
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/position.py#OverlayPositionController.commit_drag_position
---

# Move the overlay through the compositor

## Trigger

The listener moves an unlocked ordinary Wayland window without client positioning.

## Outcome

The compositor owns the move; Kotonoha does not save unverified client coordinates.
