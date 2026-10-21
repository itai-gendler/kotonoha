---
appliesTo:
- type: entity
  id: settings
  effect: changes
permits:
- actors:
  - listener
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/config_service.py#ConfigService
- kind: code
  role: implementation
  target: src/kotonoha/config/store.py#ConfigStore.load
---

# Only the listener changes Settings

Settings belong to this desktop installation and need no account. The listener changes them in Settings, from the tray lock, or by moving the overlay.
