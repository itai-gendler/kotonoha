---
availability:
- place: desktop
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
domain: general
---

# Change General settings

Choose the UI language, theme, settings-window opacity, and blur preference. UI-language changes offer restart; theme and window appearance apply to open windows.
