---
kind: alternate
routes:
  main: Main
steps:
- text: The Track position falls inside a gap in Lyrics.
  kind: condition
  entities:
  - entity: track
    effect: reads
    facts:
    - Position
  - entity: lyrics
    effect: reads
    facts:
    - Timed text
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product presents the gap using Settings.
  kind: product
  entities:
  - entity: settings
    effect: reads
    facts:
    - Interlude
    - Context lines
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/display/rules.py#interlude_at
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/content.py#OverlayContentController._show_interlude
---

# Read through an instrumental gap

## Trigger

Playback enters an intro, qualifying instrumental break, or outro.

## Outcome

An instrumental marker and optional countdown replace the current lyric line, with available surrounding lines retained and translation hidden.
