---
kind: alternate
routes:
  main: Main
steps:
- text: A matching saved choice exists and cache restoration is enabled.
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
- text: The Product restores Lyrics through the Manual selection and its Cached lyrics.
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
  - entity: manual-selection
    effect: reads
    facts:
    - Playback identity
    - Chosen lyrics
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
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.lookup_manual
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver._lookup_manual
---

# Restore the playback recording’s manual choice

## Trigger

A matching saved choice exists and cache restoration is enabled.

## Outcome

The listener’s confirmed content is restored before automatic sources or exact hints. Album changes do not change the playback binding.

## Edge cases

- If the chosen provider is no longer available, the saved choice stays stored.
- Legacy manual content without a playback binding can still restore through metadata matching; previously bound or superseded choices do not enter that fallback.

## Decision points

### Restoration form

Which saved choice is available?

- An explicit playback binding resolves → restore its provider content without automatic rematching.
- No binding resolves but an eligible unbound legacy manual entry matches → restore the best legacy manual match.
