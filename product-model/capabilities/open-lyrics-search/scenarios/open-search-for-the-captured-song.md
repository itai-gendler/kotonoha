---
kind: primary
routes:
  main: Main
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
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController.open
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_dialog.py#LyricsSearchDialog.show
---

# Open search for the captured song

## Trigger

The listener opens lyric search from the current song.

## Outcome

The listener arrives at Lyrics search; the captured song supplies a read-only duration and the prefilled query is searched automatically.

## Edge cases

- Missing artist or album may be prefilled from the active lyric metadata.
- Reopening an existing search window focuses it and retains its original playback identity.
