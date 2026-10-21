---
kind: edge
routes:
  main: Main
steps:
- text: The listener applies selected Lyrics.
  kind: actor
  actor: listener
  entities:
  - entity: lyrics
    effect: reads
    facts:
    - Provider
    - Song identity
    - Metadata
    - Timing
    - Confidence
    - Acquisition
    - Cache state
  contexts:
    main:
      place: desktop::lyrics-search
- text: The Product reports the failed save and retains the active document.
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

# Keep the display when the manual save fails

## Trigger

Saving the selected result fails.

## Outcome

The window shows an error; the playing song keeps its current lyrics and the choice is not reported as saved.
