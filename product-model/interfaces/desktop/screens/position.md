---
entities:
- entity: settings
  shows:
  - Placement
  - Click-through
  collects:
  - Placement
  - Click-through
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/pages.py#SettingsPageBuilder
---

# Position

The Settings page for where the overlay is anchored and whether it starts locked (click-through).
