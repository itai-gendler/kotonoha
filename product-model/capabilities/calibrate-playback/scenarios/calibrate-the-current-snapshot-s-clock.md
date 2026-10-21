---
kind: primary
routes:
  main: Main
steps:
- text: The external adapter submits its current position and playing status.
  kind: actor
  actor: external-adapter
  entities: []
  contexts:
    main:
      place: adapter
- text: The Product changes the Track clock observations.
  kind: product
  actor: external-adapter
  entities:
  - entity: track
    effect: changes
    facts:
    - Position
    - Playback status
  contexts:
    main:
      place: adapter
references:
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver._publish_clock
- kind: code
  role: implementation
  target: src/kotonoha/display/timeline.py#TimelineEngine
---

# Calibrate the current snapshot’s clock

## Trigger

The external adapter sends a newer clock observation for its latest snapshot.

## Outcome

The retained clock changes; the owning source calibrates the display clock and interpolation continues between observations.

## Edge cases

- A non-owning adapter can retain matching timing without publishing over the owner.
