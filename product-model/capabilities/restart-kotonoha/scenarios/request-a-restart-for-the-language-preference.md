---
kind: primary
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
- text: The Product applies the pending Settings and requests a replacement process.
  kind: product
  actor: listener
  entities:
  - entity: settings
    effect: changes
    facts:
    - UI language
    - Pending changes
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

# Request a restart for the language preference

## Trigger

A changed UI-language preference offers Restart.

## Outcome

The pending configuration is applied and a replacement process is requested; the current application exits when the launcher accepts that request.
