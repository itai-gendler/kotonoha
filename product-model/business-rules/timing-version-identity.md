---
appliesTo:
- type: entity
  id: timing-correction
references:
- kind: doc
  role: intent
  target: docs/SPEC.md
- kind: code
  role: implementation
  target: src/kotonoha/display/offsets.py#track_offset_key
- kind: code
  role: implementation
  target: src/kotonoha/display/offsets.py#_lyrics_digest
---

# A timing correction identifies one recording and exact lyric version

Normalized title, artist, album, and whole-second duration identify the recording. Provider, provider song identity, source text, timing, language, and translations identify the lyric version. Manual/cache acquisition state is excluded.
