---
kind: alternate
routes:
  main: Main
steps:
- text: The listener applies different Lyrics from the result set.
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
- text: The Product stores the new Cached lyrics and changes the Manual selection.
  kind: product
  actor: listener
  entities:
  - entity: cached-lyrics
    effect: creates
    facts:
    - Provider
    - Song identity
    - Title
    - Artist
    - Album
    - Duration
    - Content
    - Mode
    - Fetched at
    - Last used
  - entity: manual-selection
    effect: changes
    facts:
    - Chosen lyrics
  contexts:
    main:
      place: desktop::lyrics-search
- text: The Product replaces the active Lyrics while the same song remains active.
  kind: product
  actor: listener
  entities:
  - entity: lyrics
    effect: changes
    facts:
    - Acquisition
    - Cache state
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

# Replace one recording’s earlier choice

## Trigger

The original playback recording already has a manual selection.

## Outcome

The new choice replaces only that recording’s binding; other recordings retain their choices. Superseded content does not become a legacy heuristic selection.
