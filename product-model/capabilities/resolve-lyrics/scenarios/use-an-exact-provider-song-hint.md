---
kind: alternate
routes:
  main: Main
steps:
- text: The player supplies a recognized exact song hint for an enabled provider, with no restored manual choice.
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
  - entity: player
    effect: reads
    facts: []
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
- text: The Product obtains Lyrics for the exact provider song identity.
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
  target: src/kotonoha/lyrics/sources.py#ExactLyricsSource.resolve
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/workflow.py#LyricsResolutionWorkflow
---

# Use an exact provider song hint

## Trigger

The player supplies a recognized exact song hint for an enabled provider, with no restored manual choice.

## Outcome

The exact timed content is selected without ordinary metadata matching. An unsuccessful hint falls back to normal resolution.

## Edge cases

- QQ Music supplies exact song lookup; it is not a metadata-search provider.
