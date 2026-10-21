---
kind: primary
result: achieved
routes:
  main: Desktop
steps:
- text: The listener requests Settings.
  kind: actor
  actor: listener
  entities:
  - entity: settings
    effect: reads
    facts: []
  contexts:
    main:
      place: desktop::overlay
  capability: open-settings
- text: The Product stages the current Settings and opens General.
  kind: product
  actor: listener
  entities:
  - entity: settings
    effect: changes
    facts:
    - Pending changes
  contexts:
    main:
      place: desktop::general
  capability: open-settings
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
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController._open_settings_async
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog.current_config
- kind: code
  role: implementation
  target: src/kotonoha/app/config_service.py#ConfigService.apply_settings
- kind: code
  role: implementation
  target: src/kotonoha/app/services.py#RuntimeConfigApplier.apply
---

# Personalize Kotonoha successfully

## Trigger

The listener opens Settings from the overlay or tray.

## Outcome

General preferences are applied from the Settings working context.
