---
appliesTo:
- type: entity
  id: lyrics
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/search.py#LyricsSearchService.search
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/search_policy.py
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_model.py#LyricsSearchSortModel
---

# Manual search preserves provider-scoped candidate identity

Search deduplicates by provider and song identity. Up to 30 candidates per provider and 90 overall are exposed. Sorting and filtering operate on result identities so applying a visible row applies exactly that result.
