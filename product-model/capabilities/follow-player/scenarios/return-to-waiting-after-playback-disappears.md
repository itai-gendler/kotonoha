---
kind: edge
routes:
  main: Main
steps:
- text: The followed Track is no longer supplied.
  kind: condition
  entities:
  - entity: track
    effect: reads
    facts:
    - Identity
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product releases the old Track.
  kind: product
  entities:
  - entity: track
    effect: removes
    from: Lyrics available
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/providers/player_selection.py#PlayerSelector.choose
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_playback.py#MprisPlaybackCoordinator
- kind: code
  role: implementation
  target: src/kotonoha/app/source_gate.py#SourceOwnershipCoordinator
---

# Return to waiting after playback disappears

## Trigger

The followed player is no longer eligible and no replacement source is usable.

## Outcome

The old song is cleared and the overlay waits for music.
