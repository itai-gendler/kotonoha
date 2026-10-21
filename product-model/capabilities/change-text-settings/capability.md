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

# Change Text settings

Choose the lyric font and style, and independent main-line, context-line, and translation sizes. Untouched font fallback preferences are preserved.
