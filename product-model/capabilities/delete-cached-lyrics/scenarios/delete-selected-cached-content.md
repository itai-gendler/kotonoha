---
kind: primary
routes:
  main: Main
steps:
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
references:
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

# Delete selected cached content

## Trigger

The listener selects cache rows and confirms Delete.

## Outcome

Selected content and its manual bindings are removed; results report deleted and already-missing counts. The current query is refreshed.

## Edge cases

- Cancelling confirmation leaves the entries untouched.
- Deleting cached content does not immediately replace a document already in the display.
- Separate timing corrections remain stored.
