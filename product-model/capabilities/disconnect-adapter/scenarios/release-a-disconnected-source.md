---
kind: primary
routes:
  main: Main
steps:
- text: The external adapter disconnects.
  kind: actor
  actor: external-adapter
  entities: []
  contexts:
    main:
      place: adapter
- text: The Product changes the External adapter connection to absent and releases its Track.
  kind: product
  actor: external-adapter
  entities:
  - entity: external-adapter
    effect: changes
    facts:
    - Connection
  - entity: track
    effect: removes
    from: Lyrics available
  contexts:
    main:
      place: adapter
references:
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver._drop_client
---

# Release a disconnected source

## Trigger

An adapter connection closes.

## Outcome

Its retained candidate and sequence history are released. Its display is cleared only when it owned the visible content; another source’s display remains intact.
