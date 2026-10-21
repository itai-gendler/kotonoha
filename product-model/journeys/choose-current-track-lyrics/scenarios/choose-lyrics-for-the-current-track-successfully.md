---
kind: primary
result: achieved
routes:
  main: Desktop
steps:
- text: The listener opens search for the Track.
  kind: actor
  actor: listener
  entities:
  - entity: track
    effect: reads
    facts:
    - Title
    - Artist
  contexts:
    main:
      place: desktop::overlay
  capability: open-lyrics-search
- text: The Product opens the search session and creates a Search query from the captured Track and available
    Lyrics metadata.
  kind: product
  actor: listener
  entities:
  - entity: track
    effect: reads
    facts:
    - Title
    - Artist
    - Album
    - Duration
  - entity: lyrics
    effect: reads
    facts:
    - Metadata
  - entity: search-query
    effect: creates
    facts: &id001
    - Title
    - Artist
    - Album
    - Duration
    - Playback identity
    - Providers
  contexts:
    main:
      place: desktop::lyrics-search
  capability: open-lyrics-search
- text: The listener edits and submits the Search query, retaining its captured duration.
  kind: actor
  actor: listener
  entities:
  - entity: search-query
    effect: changes
    facts:
    - Title
    - Artist
    - Album
  contexts:
    main:
      place: desktop::lyrics-search
  capability: search-lyrics
- text: The Product searches the Search query’s captured providers and presents Lyrics candidates.
  kind: product
  actor: listener
  entities:
  - entity: lyrics
    effect: creates
    facts:
    - Provider
    - Song identity
    - Metadata
    - Timed text
    - Timing
    - Confidence
    - Acquisition
    - Cache state
  - entity: search-query
    effect: reads
    facts: *id001
  contexts:
    main:
      place: desktop::lyrics-search
  capability: search-lyrics
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
  capability: apply-lyrics
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
  capability: apply-lyrics
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
  capability: apply-lyrics
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController.open
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_dialog.py#LyricsSearchDialog.show
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/search.py#LyricsSearchService.search
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_dialog.py#LyricsSearchDialog.set_results
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_model.py#LyricsSearchSortModel
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

# Choose lyrics for the current track successfully

## Trigger

The listener follows the overlay’s search action.

## Outcome

The search session carries the listener from the song to comparison and an applied manual choice.
