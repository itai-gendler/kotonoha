---
kind: primary
routes:
  main: Main
steps:
- text: The listener requests clearing all Cached lyrics.
  kind: actor
  actor: listener
  entities:
  - entity: cached-lyrics
    effect: reads
    facts: []
  contexts:
    main:
      place: desktop::local-lyrics-cache
- text: The Product removes all Cached lyrics and dependent Manual selection records.
  kind: product
  actor: listener
  entities:
  - entity: cached-lyrics
    effect: removes
  - entity: manual-selection
    effect: removes
    with: cached-lyrics
  contexts:
    main:
      place: desktop::local-lyrics-cache
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog._request_clear_cache
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheDialog._confirm_clear
- kind: code
  role: implementation
  target: src/kotonoha/app/cache_management.py#CacheManagementController._clear_async
---

# Clear the cache from local lyrics cache

## Trigger

The listener requests a full cache clear and confirms it in the manager.

## Outcome

Every cached record and binding is removed. Timing corrections remain separate; a currently displayed document is not replaced by this operation.

## Edge cases

- The manager refreshes its active query after a successful clear.
- The manager reports storage or refresh failures without claiming success.
