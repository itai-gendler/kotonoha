---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: README.md
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
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

# Search lyrics

Search configured metadata-search providers, compare candidate versions and confidence, sort results, and optionally show only high matches.
