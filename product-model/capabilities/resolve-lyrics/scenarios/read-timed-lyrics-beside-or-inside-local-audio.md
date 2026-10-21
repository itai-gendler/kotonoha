---
kind: alternate
routes:
  main: Main
steps:
- text: A local-audio hint is available and no saved manual choice is restored.
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
- text: The Product reads local Lyrics and retains the sidecar or embedded acquisition.
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
  target: src/kotonoha/lyrics/sources.py#LocalLyricsSource.resolve_exact
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/local.py#load_sidecar_lyrics
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/local.py#load_embedded_lyrics
---

# Read timed lyrics beside or inside local audio

## Trigger

A local-audio hint is available and no saved manual choice is restored.

## Outcome

Adjacent timed LRC wins; embedded timed tags are tried next. Local content is not written to the network cache.

## Edge cases

- Missing, unreadable, or untimed local content falls back to ordinary sources.
- Without the optional tag reader, embedded lyrics are unavailable; sidecars remain usable.
