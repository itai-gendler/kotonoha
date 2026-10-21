---
kind: primary
routes:
  main: Main
steps:
- text: The listener requests click-through.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop
- text: The Product changes Settings click-through to enabled.
  kind: product
  actor: listener
  entities:
  - entity: settings
    effect: changes
    facts:
    - Click-through
  contexts:
    main:
      place: desktop
references:
- kind: code
  role: implementation
  target: src/kotonoha/tray.py#KotonohaTray
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController._on_toggle_passthrough
---

# Lock the overlay

## Trigger

The listener chooses the corresponding lock action.

## Outcome

The overlay, tray indication, and persisted click-through preference are synchronized.

## Edge cases

- The tray remains a way to change the lock while lyric content passes pointer input through.
