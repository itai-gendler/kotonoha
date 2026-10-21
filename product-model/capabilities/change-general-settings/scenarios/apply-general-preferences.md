---
kind: primary
routes:
  main: Main
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
---

# Apply General preferences

## Trigger

The listener edits General preferences and chooses Apply or OK.

## Outcome

Only the fields edited in this form are merged into the current preferences, which take effect and are saved. A new theme or window appearance applies to open windows at once; a changed interface language offers Restart.

## Edge cases

- A newer overlay drag or tray click-through change survives when the form did not edit that field.
