---
kind: validation
routes:
  main: Main
steps:
- text: The external adapter submits a snapshot.
  kind: actor
  actor: external-adapter
  entities: []
  contexts:
    main:
      place: adapter
- text: The Product rejects the message without replacing accepted content.
  kind: product
  actor: external-adapter
  entities: []
  contexts:
    main:
      place: adapter
references:
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver._publish_snapshot
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/protocol.py#AdapterProtocolDecoder
---

# Discard an invalid or stale snapshot

## Trigger

An adapter submits an invalid document or a sequence no newer than its last accepted message.

## Outcome

The message is discarded and the accepted playback state remains unchanged.

## Edge cases

- Timed lines are validated as a complete document, not converted into partial usable lyrics.
