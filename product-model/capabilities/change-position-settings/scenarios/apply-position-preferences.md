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
    - Placement
    - Click-through
  contexts:
    main:
      place: desktop::position
- text: The Product changes Settings and refreshes the affected behavior.
  kind: product
  actor: listener
  entities:
  - entity: settings
    effect: changes
    facts:
    - Placement
    - Click-through
    - Pending changes
  contexts:
    main:
      place: desktop::position
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

# Apply Position preferences

## Trigger

The listener edits Position preferences and chooses Apply or OK.

## Outcome

Only the fields edited in this form are merged into the current preferences, which take effect and are saved.

## Edge cases

- A newer overlay drag or tray click-through change survives when the form did not edit that field.
