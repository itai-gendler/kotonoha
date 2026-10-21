---
kind: primary
routes:
  main: Main
steps:
- text: The listener opens the cache manager.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::sources
- text: The Product opens the manager and loads Cached lyrics metadata.
  kind: product
  actor: listener
  entities:
  - entity: cached-lyrics
    effect: reads
    facts:
    - Provider
    - Song identity
    - Title
    - Artist
    - Album
    - Mode
    - Fetched at
    - Last used
  contexts:
    main:
      place: desktop::local-lyrics-cache
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/cache_management.py#CacheManagementController.open
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheDialog.show
---

# Open the cache manager

## Trigger

The listener chooses Local lyrics cache in Sources.

## Outcome

The listener arrives at the cache manager and its initial unfiltered list is requested.

## Edge cases

- An already-open manager is focused rather than replaced.
