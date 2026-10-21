---
actors:
- listener
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog._request_restart
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController._restart
---

# Apply the UI language

## Goal

Use a chosen interface language across the application.

## Success criterion

The preference is applied and a restart is requested through the offered continuation.
