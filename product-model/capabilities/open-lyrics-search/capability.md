---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController.open
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_dialog.py#LyricsSearchDialog.show
---

# Open lyrics search

Open the current-track search session, prefilled from playback and available active lyric metadata.
