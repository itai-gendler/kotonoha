---
availability:
- place: desktop
references:
- kind: code
  role: implementation
  target: src/kotonoha/config/store.py#ConfigStore.load
- kind: code
  role: implementation
  target: src/kotonoha/config/models.py#Config.from_dict
---

# Restore Settings

Load persisted preferences at startup, normalizing values and falling back to defaults when saved configuration cannot be read.
