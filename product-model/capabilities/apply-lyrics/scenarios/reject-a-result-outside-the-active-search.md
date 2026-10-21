---
kind: validation
routes:
  main: Main
steps:
- text: The listener submits an obsolete candidate.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::lyrics-search
- text: The Product reports the stale result.
  kind: product
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::lyrics-search
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController._apply_async
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.select
- kind: code
  role: implementation
  target: src/kotonoha/app/display_coordinator.py#DisplayCoordinator.apply_manual_artifact
---

# Reject a result outside the active search

## Trigger

The listener applies a result that is no longer among the current results.

## Outcome

The window reports that the result is gone; no selection is persisted.
