---
actors:
- listener
references:
- kind: doc
  role: intent
  target: README.md
- kind: code
  role: implementation
  target: src/kotonoha/app/cache_management.py#CacheManagementController
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheDialog
---

# Clean the local cache

## Goal

Remove stored lyrics the listener no longer wants.

## Success criterion

Confirmed records and their bindings are removed and the manager reports the result.
