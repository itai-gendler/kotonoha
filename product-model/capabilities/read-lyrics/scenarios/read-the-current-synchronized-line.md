---
kind: primary
routes:
  main: Main
steps:
- text: A Track and its Lyrics are available.
  kind: condition
  entities:
  - entity: track
    effect: reads
    facts:
    - Position
    - Playback status
  - entity: lyrics
    effect: reads
    facts:
    - Timed text
    - Timing
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product projects Lyrics at the adjusted Track position using Settings and any Timing correction.
  kind: product
  entities:
  - entity: lyrics
    effect: reads
    facts:
    - Timed text
    - Timing
  - entity: track
    effect: reads
    facts:
    - Position
    - Playback status
  - entity: settings
    effect: reads
    facts:
    - Karaoke
    - Global lead
    - Translation
    - Context lines
    - Script
  - entity: timing-correction
    effect: reads
    facts:
    - Correction
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/display/presentation.py#DisplayEngine
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/content.py#OverlayContentController
---

# Read the current synchronized line

## Trigger

A timed document is available and the playback position is known.

## Outcome

The current line follows playback, with preceding/following lines and available translation according to preferences.

## Edge cases

- Word-timed lines use word progress when karaoke is enabled; other lines use line progress.
- Script conversion changes displayed text without changing source text or the correction identity.
- Before a lyric document or a usable position is available, title and artist provide fallback.
