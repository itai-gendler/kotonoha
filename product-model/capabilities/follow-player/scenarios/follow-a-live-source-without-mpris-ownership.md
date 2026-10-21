---
kind: alternate
routes:
  main: Main
steps:
- text: MPRIS has no playback to follow and a live source has.
  kind: condition
  entities:
  - entity: settings
    effect: reads
    facts:
    - Display sources
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product establishes the live Track for display.
  kind: product
  entities:
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

# Follow a live source without MPRIS ownership

## Trigger

MPRIS is unavailable or disabled and a live playback candidate is available.

## Outcome

An enabled live source supplies the active song: candidates with lyrics are preferred, then configured display-source order and newest candidate within that source decide.
