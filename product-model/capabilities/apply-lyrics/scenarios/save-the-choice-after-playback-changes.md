---
kind: alternate
routes:
  main: Main
steps:
- text: The listener applies the chosen Lyrics.
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
- text: The Product saves the Cached lyrics with a Manual selection for the song the search window opened for.
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
- text: The playing Track is no longer the song the search window opened for.
  kind: condition
  entities:
  - entity: track
    effect: reads
    facts:
    - Title
    - Artist
    - Duration
  contexts:
    main:
      place: desktop::lyrics-search
- text: The Product leaves the playing Track's Lyrics as they are and reports the choice as saved for the next lookup.
  kind: product
  actor: listener
  entities:
  - entity: track
    effect: reads
    facts: []
  - entity: lyrics
    effect: reads
    facts: []
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

# Save the choice after playback changes

## Trigger

The listener applies a search result after the player has moved on to a different song.

## Outcome

The choice is saved for the song the search window opened for, and the song now playing keeps its lyrics. The window says the lyrics are saved as manual and will be used the next time that song is looked up.

## Edge cases

- When the original song plays again, its saved choice is restored before any automatic source.
