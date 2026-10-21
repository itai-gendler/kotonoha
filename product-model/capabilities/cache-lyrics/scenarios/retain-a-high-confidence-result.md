---
kind: primary
routes:
  main: Main
steps:
- text: The Lyrics match is high confidence and automatic caching is enabled.
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
- text: The Product creates Cached lyrics for later reuse.
  kind: product
  entities:
  - entity: cached-lyrics
    effect: creates
    facts:
    - Provider
    - Song identity
    - Title
    - Artist
    - Album
    - Duration
    - Content
    - Mode
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

# Retain a high-confidence result

## Trigger

Automatic resolution obtains a cacheable high-confidence document with caching enabled.

## Outcome

Content is stored under its provider and song identity with automatic mode and refreshed timestamps.

## Edge cases

- Medium-confidence results are not automatically stored.
- Local sidecar, embedded, and live documents do not use this network-content cache path.
- A cache write failure does not prevent the resolved lyrics from being displayed.
