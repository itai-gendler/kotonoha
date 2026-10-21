---
entities:
- entity: track
  shows:
  - Title
  - Artist
- entity: lyrics
  shows:
  - Timed text
  - Timing
- entity: timing-correction
  shows:
  - Correction
- entity: settings
  shows:
  - Click-through
  - Placement
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/content.py#OverlayContentController
---

# Lyrics overlay

The current song, synchronized words and lines, available translation, instrumental gaps, and timing feedback.
