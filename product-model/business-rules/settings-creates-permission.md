---
appliesTo:
- type: entity
  id: settings
  effect: creates
permits:
- unattended: true
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/config_service.py#ConfigService
- kind: code
  role: implementation
  target: src/kotonoha/config/store.py#ConfigStore.load
---

# Kotonoha establishes Settings when it starts

At startup Kotonoha loads the saved preferences, or uses defaults when none can be read.
