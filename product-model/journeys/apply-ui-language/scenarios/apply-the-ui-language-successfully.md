---
kind: primary
result: achieved
routes:
  main: Desktop
steps:
- text: The listener edits the selected Settings values and applies them.
  kind: actor
  actor: listener
  entities:
  - entity: settings
    effect: reads
    facts:
    - UI language
    - Theme
    - Window appearance
  contexts:
    main:
      place: desktop::general
  capability: change-general-settings
- text: The Product changes Settings and refreshes the affected behavior.
  kind: product
  actor: listener
  entities:
  - entity: settings
    effect: changes
    facts:
    - UI language
    - Theme
    - Window appearance
    - Pending changes
  contexts:
    main:
      place: desktop::general
  capability: change-general-settings
- text: The listener requests Restart.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::general
  capability: restart-kotonoha
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
  capability: restart-kotonoha
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog.current_config
- kind: code
  role: implementation
  target: src/kotonoha/app/config_service.py#ConfigService.apply_settings
- kind: code
  role: implementation
  target: src/kotonoha/app/services.py#RuntimeConfigApplier.apply
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog._request_restart
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController._restart
---

# Apply the UI language successfully

## Trigger

The listener changes the UI language in General.

## Outcome

The settings workflow applies the preference and requests relaunch; launcher failure keeps the current process running.
