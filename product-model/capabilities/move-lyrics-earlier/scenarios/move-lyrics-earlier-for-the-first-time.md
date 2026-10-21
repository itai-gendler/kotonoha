---
kind: primary
routes:
  main: Main
steps:
- text: The listener requests earlier lyrics.
  kind: actor
  actor: listener
  entities:
  - entity: lyrics
    effect: reads
    facts:
    - Timed text
  contexts:
    main:
      place: desktop::overlay
- text: The Product creates a Timing correction of plus 100 milliseconds for this version.
  kind: product
  actor: listener
  entities:
  - entity: timing-correction
    effect: creates
    facts:
    - Recording
    - Lyric version
    - Correction
  contexts:
    main:
      place: desktop::overlay
- text: The Product reprojects Lyrics with the new correction.
  kind: product
  actor: listener
  entities:
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
  target: src/kotonoha/ui/overlay/content.py#OverlayContentController
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController._handle_intent
- kind: code
  role: implementation
  target: src/kotonoha/app/track_offset_service.py#TrackOffsetService
---

# Move lyrics earlier for the first time

## Trigger

The listener adjusts timing while a usable lyric version is displayed.

## Outcome

The first correction is applied immediately, its value is shown briefly, and persistence is scheduled. The source lyric timestamps remain unchanged.

## Edge cases

- No usable version identity means no timing adjustment is made.
- Values are clamped to minus ten through plus ten seconds.
