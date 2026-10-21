---
kind: primary
routes:
  main: Main
steps:
- text: The listener closes the cache manager.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::local-lyrics-cache
- text: The Product cancels window-owned pending work.
  kind: product
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::local-lyrics-cache
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/cache_management.py#CacheManagementController._clear_dialog
---

# Close the cache manager

## Trigger

The listener closes Local lyrics cache.

## Outcome

The window closes and pending completions cannot update the closed window.

## Edge cases

- An already-running storage operation can finish; closing does not roll back completed deletions.
