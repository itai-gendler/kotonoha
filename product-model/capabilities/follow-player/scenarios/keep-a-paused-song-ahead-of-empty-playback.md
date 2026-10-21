---
kind: alternate
routes:
  main: Main
steps:
- text: The current Player candidates have incomplete playing metadata.
  kind: condition
  entities:
  - entity: player
    effect: reads
    facts:
    - Name
    - Track metadata
    - Playback status
    - Current
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product follows the paused Player and records its Track.
  kind: product
  entities:
  - entity: player
    effect: changes
    facts:
    - Current
  - entity: track
    effect: creates
    to: Detected
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

# Keep a paused song ahead of empty playback

## Trigger

No playing candidate has track metadata, but a paused candidate does.

## Outcome

The current paused player with metadata wins, otherwise another paused player with metadata wins before a playing player with no metadata.
