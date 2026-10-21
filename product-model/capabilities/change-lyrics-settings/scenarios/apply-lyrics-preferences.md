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
    - Karaoke
    - Global lead
    - Translation
    - Context lines
    - Script
    - Interlude
  contexts:
    main:
      place: desktop::lyrics
- text: The Product changes Settings and refreshes the affected behavior.
  kind: product
  actor: listener
  entities:
  - entity: settings
    effect: changes
    facts:
    - Karaoke
    - Global lead
    - Translation
    - Context lines
    - Script
    - Interlude
    - Pending changes
  contexts:
    main:
      place: desktop::lyrics
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

# Apply Lyrics preferences

## Trigger

The listener edits Lyrics preferences and chooses Apply or OK.

## Outcome

Only the fields edited in this form are merged into the current preferences, which take effect and are saved.

## Edge cases

- A newer overlay drag or tray click-through change survives when the form did not edit that field.
