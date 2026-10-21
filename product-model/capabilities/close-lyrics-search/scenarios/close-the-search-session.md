---
kind: primary
routes:
  main: Main
steps:
- text: The listener closes the search window.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::lyrics-search
- text: The Product stops the window’s pending searches and removes the Search query.
  kind: product
  actor: listener
  entities:
  - entity: search-query
    effect: removes
  contexts:
    main:
      place: desktop::lyrics-search
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController._clear_dialog
---

# Close the search session

## Trigger

The listener closes Lyrics search.

## Outcome

The window closes and stale search completions cannot update it. A completed manual save remains persisted.

## Edge cases

- A save already in progress may still complete; closing does not undo saved lyrics.
