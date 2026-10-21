---
kind: primary
routes:
  main: Main
steps:
- text: Eligible playback is observed.
  kind: condition
  entities:
  - entity: settings
    effect: reads
    facts:
    - Player preference
    - Display sources
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product records Player information and selects the active instance.
  kind: product
  entities:
  - entity: player
    effect: creates
    facts:
    - Name
    - Track metadata
    - Playback status
    - Current
  contexts:
    main:
      place: desktop::overlay
- text: The Product establishes a Track after its metadata settles.
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

# Follow stable MPRIS playback

## Trigger

Kotonoha observes eligible MPRIS playback.

## Outcome

The selected player supplies stable track facts for lyric lookup. A stopped player is not followed.

## Decision points

### Preferred player

Which player supplies the active song?

- A preferred player is Playing or Paused → follow it, including a paused preferred player.
- The preference is absent or not eligible → use automatic ranking and retain the saved preference.
