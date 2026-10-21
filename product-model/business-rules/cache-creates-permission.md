---
appliesTo:
- type: entity
  id: cached-lyrics
  effect: creates
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController._apply_async
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver
permits:
- actors:
  - listener
- unattended: true
  when:
  - entity: settings
    fact: Cache enabled
    is: true
---

# Only the listener's choices are saved while the cache is off

Applying a search result saves it even while the cache is disabled. Lyrics found automatically are saved only while Cache enabled is on.
