---
kind: primary
routes:
  main: Main
steps:
- text: The listener moves the unlocked overlay.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::overlay
- text: The Product saves the accepted Settings placement.
  kind: product
  actor: listener
  entities:
  - entity: settings
    effect: changes
    facts:
    - Placement
    - Saved output
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

# Save a successful overlay move

## Trigger

The listener moves an unlocked overlay on a platform that supports client positioning.

## Outcome

A successfully completed move stores output-relative placement and output geometry; a failed movement is not persisted as an achieved position.

## Edge cases

- Where the compositor binds the overlay to one output, the panel stays within that output.
- Where the overlay can move between displays, releasing it on another display moves it there; the position is saved only after that succeeds.
