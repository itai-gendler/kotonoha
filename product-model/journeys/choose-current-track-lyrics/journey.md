---
actors:
- listener
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_dialog.py#LyricsSearchDialog
---

# Choose lyrics for the current track

## Goal

Replace a missing or unsuitable lyric match.

## Success criterion

A chosen result is bound to the original playback recording and displayed when that song remains active.
