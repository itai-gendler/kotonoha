---
kind: edge
routes:
  main: Main
steps:
- text: The listener confirms deletion of Cached lyrics.
  kind: actor
  actor: listener
  entities:
  - entity: cached-lyrics
    effect: reads
    facts:
    - Provider
    - Song identity
  contexts:
    main:
      place: desktop::local-lyrics-cache
- text: The Product removes Cached lyrics and dependent Manual selection records.
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
- text: The Product reports the completed deletion and failed refresh.
  kind: product
  actor: listener
  entities: []
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

# Report deletion even if refresh fails

## Trigger

Selected entries are deleted but reloading the metadata list fails.

## Outcome

The manager reports actual deletion results and a separate refresh failure.

## Edge cases

- If deletion itself fails, the manager reports a deletion error rather than successful deletion.
