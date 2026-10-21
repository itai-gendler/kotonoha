---
kind: validation
routes:
  main: Main
steps:
- text: The listener submits empty title and artist.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::lyrics-search
- text: The Product reports the missing query.
  kind: product
  actor: listener
  entities: []
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

# Reject a query without title or artist

## Trigger

The listener submits empty or whitespace-only title and artist.

## Outcome

The window reports that a query is needed; album alone does not start a provider search.
