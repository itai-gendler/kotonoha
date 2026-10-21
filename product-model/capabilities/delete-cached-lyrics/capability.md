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
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheDialog._confirm_delete
- kind: code
  role: implementation
  target: src/kotonoha/app/cache_management.py#CacheManagementController._delete_async
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.delete_many
domain: local-lyrics-cache
---

# Delete cached lyrics

Delete the selected provider-scoped cache entries after confirmation and refresh the current query.
