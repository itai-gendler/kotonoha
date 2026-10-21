---
kind: alternate
routes:
  main: Desktop
steps:
- text: The active Track needs a new resolution while cache use is disabled.
  kind: condition
  entities:
  - entity: track
    effect: reads
    facts:
    - Title
    - Artist
  - entity: settings
    effect: reads
    facts:
    - Cache enabled
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product starts resolving the Track without reading the cache.
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
- text: The Product resolves Lyrics from the configured sources for the Track.
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
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver
---

# Resolve with cache disabled

## Trigger

A stable MPRIS song is resolved while Cache enabled is false.

## Outcome

Automatic resolution skips persistent-cache reads and writes, including restoration of a saved manual choice. It still obtains usable content from configured sources. Existing saved content remains stored.

## Edge cases

- A manual document already applied to the current song remains its display override until a track change; disabling automatic restoration does not erase it.
