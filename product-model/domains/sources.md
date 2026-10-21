---
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog
---

# Sources

Where playback and lyrics come from: which player Kotonoha follows, the order of lyric providers and display sources, how lyrics are resolved and cached, and access to the Local lyrics cache.

## Boundary

Owns player selection, source policy, lyric acquisition, and access to Local lyrics cache. Does not own presentation effects or recording timing corrections.
