---
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/cache_dialog.py#LyricsCacheDialog
---

# Local lyrics cache

The Local lyrics cache manager: finding stored lyrics by their metadata and deleting the entries the listener no longer wants.

## Boundary

Owns browsing and deletion of stored lyric content. Does not own editing lyric text or choosing replacement lyrics.
