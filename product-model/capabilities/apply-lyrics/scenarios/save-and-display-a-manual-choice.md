---
kind: primary
routes:
  main: Main
steps:
- text: The listener applies the selected Lyrics.
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
- text: The Product creates Cached lyrics and its Manual selection for the original playback identity.
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
    effect: creates
    facts:
    - Playback identity
    - Chosen lyrics
    with: cached-lyrics
  contexts:
    main:
      place: desktop::lyrics-search
- text: The Product displays the selected Lyrics for the matching Track.
  kind: product
  actor: listener
  entities:
  - entity: lyrics
    effect: changes
    facts:
    - Acquisition
    - Cache state
  - entity: track
    effect: changes
    from: Lyrics not found
    to: Lyrics available
    facts:
    - Lyric status
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

# Save and display a manual choice

## Trigger

The current song has no timed lyrics. The listener selects a current search result and chooses Apply lyrics.

## Outcome

The content and playback binding are committed together. The selected lyrics replace the active document at the current playback position, and the source status refreshes.

## Edge cases

- The current manually applied row is marked Applied; selecting it again does not submit another application.
- Edited query fields and provider metadata never redefine the original playback binding.
