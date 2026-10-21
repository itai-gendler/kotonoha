---
kind: alternate
routes:
  main: Main
steps:
- text: The Track has a new playback observation.
  kind: condition
  entities:
  - entity: track
    effect: reads
    facts:
    - Position
    - Playback status
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product recalibrates the Track and projects Lyrics from the resulting time.
  kind: product
  entities:
  - entity: track
    effect: changes
    facts:
    - Position
    - Playback status
  - entity: lyrics
    effect: reads
    facts:
    - Timed text
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/display/timeline.py#TimelineEngine
- kind: code
  role: implementation
  target: src/kotonoha/clock.py#MediaClock
---

# Follow pause, resume, and seeking

## Trigger

A playback observation changes position or playing status.

## Outcome

A known position is interpolated while reports advance or the source reports Playing. A non-playing source with stalled position is confirmed paused after the 1.5-second grace; the clock then anchors to its reported time. Later playback and seek observations recalibrate display.
