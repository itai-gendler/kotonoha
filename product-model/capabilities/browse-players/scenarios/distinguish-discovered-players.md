---
kind: primary
routes:
  main: Main
steps:
- text: The listener inspects Player entries.
  kind: actor
  actor: listener
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
      place: desktop::sources
references:
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_playback.py#MprisPlaybackCoordinator.available_players
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/sources.py#SettingsSourcesPageBuilder.build
---

# Distinguish discovered players

## Trigger

The listener opens Sources after player discovery.

## Outcome

The list identifies player instances with playback metadata and the policy-selected player. A saved but absent preference is marked unavailable.

## Edge cases

- The player list is captured when Settings opens; opening an already-open Settings window does not rediscover players.
