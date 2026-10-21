---
entities:
- entity: settings
  shows:
  - Panel
  - Panel opacity
  - Panel tint
  collects:
  - Panel
  - Panel opacity
  - Panel tint
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/pages.py#SettingsPageBuilder
---

# Panel

The Settings page for the panel behind the lyrics: its style, width, long-line behavior, opacity and accent tint.
