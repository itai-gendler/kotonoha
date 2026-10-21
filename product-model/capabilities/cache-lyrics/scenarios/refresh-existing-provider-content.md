---
kind: alternate
routes:
  main: Main
steps:
- text: A cacheable Lyrics result has an existing record.
  kind: condition
  entities:
  - entity: lyrics
    effect: reads
    facts:
    - Confidence
    - Provider
    - Song identity
  - entity: settings
    effect: reads
    facts:
    - Cache enabled
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product refreshes the existing Cached lyrics in place.
  kind: product
  entities:
  - entity: cached-lyrics
    effect: changes
    facts:
    - Title
    - Artist
    - Album
    - Duration
    - Content
    - Fetched at
    - Last used
  contexts:
    main:
      place: desktop::local-lyrics-cache
references:
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/__init__.py#LyricsCache.store
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver
---

# Refresh existing provider content

## Trigger

A high-confidence automatic result arrives for content already cached automatically under the same provider and song identity.

## Outcome

The record's content and timestamps are refreshed in place; it stays one entry for that provider and song.
