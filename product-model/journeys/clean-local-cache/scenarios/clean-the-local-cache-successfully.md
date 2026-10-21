---
kind: primary
result: achieved
routes:
  main: Desktop
steps:
- text: The listener opens the cache manager.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::sources
  capability: open-local-lyrics-cache
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
  capability: open-local-lyrics-cache
- text: The listener searches the local cache.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::local-lyrics-cache
  capability: browse-cached-lyrics
- text: The Product presents matching Cached lyrics in recent-use order.
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
  capability: browse-cached-lyrics
- text: The listener selects Cached lyrics and confirms deletion.
  kind: actor
  actor: listener
  entities:
  - entity: cached-lyrics
    effect: reads
    facts:
    - Provider
    - Song identity
    - Title
  contexts:
    main:
      place: desktop::local-lyrics-cache
  capability: delete-cached-lyrics
- text: The Product removes Cached lyrics and each dependent Manual selection.
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
  capability: delete-cached-lyrics
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/cache_management.py#CacheManagementController.open
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheDialog.show
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.search
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheTableModel
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheDialog._confirm_delete
- kind: code
  role: implementation
  target: src/kotonoha/app/cache_management.py#CacheManagementController._delete_async
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.delete_many
---

# Clean the local cache successfully

## Trigger

The listener opens Local lyrics cache from Sources.

## Outcome

The listener reaches the independent manager and deletes selected stored content.
