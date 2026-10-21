---
kind: validation
routes:
  main: Main
steps:
- text: The external adapter submits a clock observation.
  kind: actor
  actor: external-adapter
  entities: []
  contexts:
    main:
      place: adapter
- text: The Product leaves the accepted clock unchanged.
  kind: product
  actor: external-adapter
  entities: []
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

# Discard a clock for another song

## Trigger

The clock refers to a different track, precedes a usable snapshot, or repeats an accepted sequence.

## Outcome

The current display is unchanged; an unaccepted wrong-track clock does not consume its sequence.
