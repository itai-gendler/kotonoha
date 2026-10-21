---
appliesTo:
- type: entity
  id: manual-selection
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#_selection_key
- kind: code
  role: implementation
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController.open
---

# A manual selection belongs to the original playback identity

The identity is the exact playback title and artist plus duration rounded to 0.1 seconds. Album is excluded. Search edits and provider metadata do not redefine it. A replacement changes only that playback identity’s choice.
