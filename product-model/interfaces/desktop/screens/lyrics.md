---
entities:
- entity: settings
  shows:
  - Karaoke
  - Global lead
  - Translation
  - Context lines
  - Script
  - Interlude
  collects:
  - Karaoke
  - Global lead
  - Translation
  - Context lines
  - Script
  - Interlude
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/pages.py#SettingsPageBuilder
---

# Lyrics

The Settings page for how lyrics are shown: karaoke highlighting, the global timing lead, translations, context lines, Chinese script conversion and instrumental gaps.
