---
kind: alternate
routes:
  main: Main
steps:
- text: Cider is enabled in the lyric sources and its active song changes.
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
- text: The Product fetches the current Cider Lyrics.
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
  target: src/kotonoha/providers/cider_api.py#CiderApiProvider._poll_once
- kind: code
  role: implementation
  target: src/kotonoha/providers/cider_api.py#CiderApiProvider._load_lyrics
---

# Resolve Cider lyrics

## Trigger

Cider is enabled in the lyric sources and its active song changes.

## Outcome

The complete timed document is fetched for the current Cider song; subsequent playback observations calibrate time without refetching each frame.

## Edge cases

- A lyric request failure leaves a no-lyrics result for that attempt.
- Content arriving for an older song is discarded.
- Changing the translation-language configuration initiates a fresh lyric request.
