---
kind: primary
routes:
  main: Main
steps:
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
    facts:
    - Title
    - Artist
    - Album
    - Duration
    - Playback identity
    - Providers
  contexts:
    main:
      place: desktop::lyrics-search
references:
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/search.py#LyricsSearchService.search
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_dialog.py#LyricsSearchDialog.set_results
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_model.py#LyricsSearchSortModel
---

# Compare lyric search results

## Trigger

The search window opens or the listener submits edited title, artist, and album.

## Outcome

Usable candidates appear with provider, metadata, duration, timing/format, translation indication, and confidence. Results start in descending match order; sorting or filtering retains correct result identity.

## Edge cases

- Up to 30 candidates per provider and 90 overall are exposed, deduplicated by provider and song identity.
- An existing active lyric result is marked when present; choosing another row does not change the active document.
- Only one search or application operation owns the window at a time.
