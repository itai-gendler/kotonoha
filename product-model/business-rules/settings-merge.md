---
appliesTo:
- type: entity
  id: settings
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/config_merge.py#merge_settings
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/form_state.py#SettingsFormState
---

# Applying Settings changes only fields edited in the form

An open form may predate overlay movement or a tray lock action. Only edited settings fields are merged into current preferences; detected output geometry remains owned by runtime placement. Reset is per-section and stays pending until applied.
