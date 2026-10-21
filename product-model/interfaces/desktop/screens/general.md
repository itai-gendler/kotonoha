---
entities:
- entity: settings
  shows:
  - UI language
  - Theme
  - Window appearance
  collects:
  - UI language
  - Theme
  - Window appearance
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/pages.py#SettingsPageBuilder
---

# General

The Settings page that opens first: interface language, theme, and the Settings window's own blur and opacity.
