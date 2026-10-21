---
kind: alternate
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
- text: The Product changes the Timing correction and schedules its latest value for persistence.
  kind: product
  actor: listener
  entities:
  - entity: timing-correction
    effect: changes
    facts:
    - Correction
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

# Adjust an existing correction earlier

## Trigger

The listener adjusts a version that already has a correction.

## Outcome

The correction changes by one 100-millisecond step within its bounds and the active display changes immediately.

## Edge cases

- The state store retains corrections without an arbitrary entry-count limit.
