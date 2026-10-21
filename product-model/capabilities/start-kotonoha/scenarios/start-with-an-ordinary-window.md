---
kind: alternate
routes:
  main: Desktop
steps:
- text: The listener launches Kotonoha.
  kind: actor
  entities: []
  contexts:
    main:
      place: desktop::overlay
  actor: listener
- text: The Product opens the overlay using the supported platform behavior.
  kind: product
  entities: []
  contexts:
    main:
      place: desktop::overlay
  actor: listener
references:
- kind: code
  role: implementation
  target: src/kotonoha/platform/window_platform.py
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/window.py#LyricsOverlay.activate_layer_shell
---

# Start with an ordinary window

## Trigger

The listener starts Kotonoha where Layer Shell is unavailable.

## Outcome

Kotonoha uses an ordinary window. Background blur is independently available only when supported; otherwise the panel remains translucent without blur.

## Edge cases

- Fullscreen stacking is not guaranteed for an ordinary window.
