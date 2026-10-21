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
---

# Change Icon settings

Choose the tray icon and window/taskbar icon independently. Generated icons follow the configured accent.
