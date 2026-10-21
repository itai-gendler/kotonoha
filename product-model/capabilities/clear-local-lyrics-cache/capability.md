---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: README.md
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog._request_clear_cache
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheDialog._confirm_clear
- kind: code
  role: implementation
  target: src/kotonoha/app/cache_management.py#CacheManagementController._clear_async
domain: sources
---

# Clear Local lyrics cache

Remove all stored lyric content and its playback bindings from Sources or the cache manager.
