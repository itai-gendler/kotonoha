---
kind: primary
routes:
  main: Main
steps:
- text: A stable song has no restored manual choice or usable exact hint.
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
- text: The Product obtains Lyrics from the configured sources and selects the winning match.
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
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/workflow.py#LyricsResolutionWorkflow
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_lyrics.py#MprisLyricsCoordinator
---

# Choose an automatic lyric match

## Trigger

A stable song has no restored manual choice or usable exact hint.

## Outcome

The selected timed document becomes available for the current song.

## Edge cases

- A provider’s highest-ranked candidate with no timed lines may fall through to another usable candidate.
- A source failure permits remaining sources to answer and is distinct from a normal miss.

## Decision points

### Source policy

How is the automatic candidate selected?

- Prefer best match is enabled → compare cache and matching live candidates first, request only network sources that can improve the answer, rank confidence before configured order.
- Prefer best match is disabled → take the first valid result in configured source order, considering each provider’s cache at that provider’s position.
