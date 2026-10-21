---
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_dialog.py#LyricsSearchDialog
---

# Search query

A query retained by the open lyric-search session, independently of the original playback identity to which a later selection is bound.

## Information kept

- **Title** — The editable title sent to metadata-search providers.
- **Artist** — The editable artist sent to metadata-search providers.
- **Album** — The editable album sent to metadata-search providers.
- **Duration** — The read-only playback duration captured when the window opens.
- **Playback identity** — The original playback recording captured when the window opens.
- **Providers** — The enabled source list captured for this search session.
