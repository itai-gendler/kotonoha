---
appliesTo:
- type: entity
  id: cached-lyrics
  effect: changes
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

# Only the listener's choices update cached lyrics while the cache is off

Applying a search result whose content is already cached marks it as the listener's choice even while the cache is disabled. Automatic refreshes of cached content happen only while Cache enabled is on.
