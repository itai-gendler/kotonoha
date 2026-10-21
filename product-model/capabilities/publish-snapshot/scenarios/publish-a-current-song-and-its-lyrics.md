---
kind: primary
routes:
  main: Main
steps:
- text: The external adapter submits current playback and a complete lyric document.
  kind: actor
  actor: external-adapter
  entities: []
  contexts:
    main:
      place: adapter
- text: The Product records the adapter Track and Lyrics.
  kind: product
  actor: external-adapter
  entities:
  - entity: track
    effect: creates
    to: Lyrics available
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
  - entity: lyrics
    effect: creates
    facts:
    - Provider
    - Song identity
    - Metadata
    - Timed text
    - Timing
    - Confidence
    - Acquisition
    - Cache state
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

# Publish a current song and its lyrics

## Trigger

An external adapter connects or its current song or lyric document changes.

## Outcome

The snapshot is kept as a live source. It is shown when the display-source order gives this adapter the playback; otherwise it is kept without replacing what is shown.

## Edge cases

- A valid snapshot may have no lyric document and still report playback.
- Provider identity belongs to the lyric document; it remains distinct from adapter and player identity.
- A reconnection starts a fresh sequence space and begins with a complete snapshot.
