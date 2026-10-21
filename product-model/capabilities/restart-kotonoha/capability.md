---
availability:
- place: desktop
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog._request_restart
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController._restart
domain: general
---

# Restart Kotonoha

Apply pending settings and request a replacement process when a UI-language change requires a restart.
