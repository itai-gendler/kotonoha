---
entities:
- entity: settings
  shows:
  - Player preference
  - Lyric sources
  - Display sources
  - Prefer best match
  - Fuzzy matching
  - Cache enabled
  collects:
  - Player preference
  - Lyric sources
  - Display sources
  - Prefer best match
  - Fuzzy matching
  - Cache enabled
  - Cider token
- entity: player
  shows:
  - Name
  - Track metadata
  - Playback status
  - Current
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/sources.py#SettingsSourcesPageBuilder
---

# Sources

The Settings page for where playback and lyrics come from: the followed player, lyric providers and display sources in order, matching and cache preferences, the Cider API token, and the way into the Local lyrics cache.
