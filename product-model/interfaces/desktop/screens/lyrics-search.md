---
entities:
- entity: track
  shows:
  - Title
  - Artist
  - Album
  - Duration
  - Playback source
- entity: lyrics
  shows:
  - Provider
  - Song identity
  - Metadata
  - Timing
  - Confidence
  - Acquisition
  - Cache state
- entity: manual-selection
  collects:
  - Chosen lyrics
- entity: search-query
  shows:
  - Title
  - Artist
  - Album
  - Duration
  collects:
  - Title
  - Artist
  - Album
references:
- kind: doc
  role: intent
  target: README.md
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_dialog.py#LyricsSearchDialog
---

# Lyrics search

Search candidates for the playback recording captured when this window opens; compare them with the active lyric source.
