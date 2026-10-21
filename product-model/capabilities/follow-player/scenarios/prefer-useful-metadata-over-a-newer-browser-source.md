---
kind: alternate
routes:
  main: Main
steps:
- text: Competing Player entries are available.
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
- text: The Product follows the better Player metadata and records the Track.
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

# Prefer useful metadata over a newer browser source

## Trigger

Two playing players describe the same listening session; the newer player has no performer.

## Outcome

The player naming a performer wins before recency is considered. For equally useful candidates, a rival must start more than one second later to win on recency.
