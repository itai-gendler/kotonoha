---
entities:
- entity: cached-lyrics
  shows:
  - Provider
  - Song identity
  - Title
  - Artist
  - Album
  - Mode
  - Fetched at
  - Last used
references:
- kind: doc
  role: intent
  target: README.md
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheDialog
---

# Local lyrics cache

Search stored lyric metadata and remove selected entries or all cached content.
