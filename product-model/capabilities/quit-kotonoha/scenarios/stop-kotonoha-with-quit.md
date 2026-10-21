---
kind: primary
routes:
  main: Main
steps:
- text: The listener chooses Quit.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::overlay
- text: The Product closes its windows and stops playback observation and display work.
  kind: product
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController.stop
- kind: code
  role: implementation
  target: src/kotonoha/tray.py#KotonohaTray
---

# Stop Kotonoha with Quit

## Trigger

The listener chooses Quit.

## Outcome

Windows close, owned input and display work stops, and scheduled settings and timing writes finish before their owners close.

## Edge cases

- A component cleanup failure is logged while cleanup of the remaining components continues.
