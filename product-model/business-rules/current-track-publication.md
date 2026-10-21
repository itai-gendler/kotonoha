---
appliesTo:
- type: entity
  id: track
- type: entity
  id: lyrics
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_lyrics.py#MprisLyricsCoordinator._load_song
- kind: code
  role: implementation
  target: src/kotonoha/app/display_coordinator.py#DisplayCoordinator
---

# Only current-track lyric work changes the active display

A lyric lookup that finishes after the song has changed is discarded. An immediate manual application checks compatibility with the captured playback song, and its display override ends when the active track changes.
