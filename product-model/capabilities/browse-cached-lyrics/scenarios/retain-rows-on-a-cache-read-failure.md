---
kind: edge
routes:
  main: Main
steps:
- text: The listener requests cache results.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::local-lyrics-cache
- text: The Product reports the failed search.
  kind: product
  actor: listener
  entities: []
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

# Retain rows on a cache read failure

## Trigger

A cache search fails.

## Outcome

The manager reports a search error, re-enables commands, and retains the previous rows.
