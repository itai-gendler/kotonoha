---
actors:
- listener
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController._open_settings_async
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog
---

# Personalize Kotonoha

## Goal

Change general preferences from the running overlay.

## Success criterion

The selected general preferences are applied and scheduled for persistence.
