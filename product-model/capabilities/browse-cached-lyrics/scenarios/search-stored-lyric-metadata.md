---
kind: primary
routes:
  main: Main
steps:
- text: The listener searches the local cache.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::local-lyrics-cache
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
references:
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.search
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheTableModel
---

# Search stored lyric metadata

## Trigger

The manager opens or the listener submits a keyword.

## Outcome

The list shows matching metadata, source identity, mode, fetch time, and last use. An empty query lists all entries.

## Edge cases

- Metadata matching ignores case and finds a contained keyword in any searchable field.
- The cache manager has no lyric-text editing action.
