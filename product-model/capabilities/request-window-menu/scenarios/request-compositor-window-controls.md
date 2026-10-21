---
kind: primary
routes:
  main: Main
steps:
- text: The listener requests window controls.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::overlay
- text: The Product asks the compositor for its system window menu.
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
  target: src/kotonoha/platform/qt_window.py
---

# Request compositor window controls

## Trigger

The listener requests the system window menu on an unlocked overlay with platform support.

## Outcome

The request is passed to the compositor; menu availability and Always on Top behavior remain compositor decisions.

## Edge cases

- Ordinary Wayland stacking does not promise visibility above fullscreen windows or persistence across surface recreation.
