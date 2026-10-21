---
kind: alternate
routes:
  main: Main
steps:
- text: An enabled provider has a compatible high-confidence cached result and cache use is enabled.
  kind: condition
  entities:
  - entity: track
    effect: reads
    facts:
    - Title
    - Artist
    - Album
    - Duration
  - entity: settings
    effect: reads
    facts:
    - Lyric sources
    - Prefer best match
    - Fuzzy matching
    - Cache enabled
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product starts resolving the Track.
  kind: product
  entities:
  - entity: track
    effect: changes
    from: Detected
    to: Resolving
    facts:
    - Lyric status
  contexts:
    main:
      place: desktop::overlay
- text: The Product restores Lyrics from the provider’s Cached lyrics.
  kind: product
  entities:
  - entity: lyrics
    effect: creates
    facts:
    - Provider
    - Song identity
    - Metadata
    - Timed text
    - Timing
    - Confidence
    - Acquisition
    - Cache state
  - entity: cached-lyrics
    effect: changes
    facts:
    - Last used
  contexts:
    main:
      place: desktop::overlay
- text: The Product makes the selected Lyrics available for the Track.
  kind: product
  entities:
  - entity: lyrics
    effect: reads
    facts:
    - Timed text
    - Provider
  - entity: track
    effect: changes
    from: Resolving
    to: Lyrics available
    facts:
    - Lyric status
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.lookup
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver
---

# Reuse a provider’s automatic cache

## Trigger

An enabled provider has a compatible high-confidence cached result and cache use is enabled.

## Outcome

The cached content participates at its owning provider’s position and successful use refreshes recency.
