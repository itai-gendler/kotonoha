---
kind: alternate
routes:
  main: Main
steps:
- text: The external adapter submits playback without a timed document.
  kind: actor
  actor: external-adapter
  entities: []
  contexts:
    main:
      place: adapter
- text: The Product records a Track with no timed document.
  kind: product
  actor: external-adapter
  entities:
  - entity: track
    effect: creates
    to: Lyrics not found
    facts:
    - Title
    - Artist
    - Album
    - Duration
    - Playback source
    - Playback status
    - Position
    - Lyric status
    - Identity
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

# Publish playback without lyric content

## Trigger

The adapter has current playback but no complete timed lyrics.

## Outcome

The song metadata is retained and can supply fallback display without inventing lyric lines.
