---
kind: edge
routes:
  main: Main
steps:
- text: The listener requests Restart.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::general
- text: The Product keeps the current application after the replacement request fails.
  kind: product
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::general
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog._request_restart
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController._restart
---

# Keep the application when relaunch fails

## Trigger

The listener requests Restart but the process launcher refuses.

## Outcome

The current application remains running; the failure is logged.
