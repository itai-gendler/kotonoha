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

# Change Panel settings

Choose panel style, automatic or fixed width, long-line scrolling or wrapping, opacity, and accent tint. Ordinary and frosted opacity values are retained separately.
