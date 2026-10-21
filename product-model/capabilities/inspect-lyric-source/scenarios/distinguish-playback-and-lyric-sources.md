---
kind: primary
routes:
  main: Main
steps:
- text: The listener inspects Lyrics source facts and the Track playback source.
  kind: actor
  actor: listener
  entities:
  - entity: lyrics
    effect: reads
    facts:
    - Provider
    - Song identity
    - Acquisition
    - Cache state
    - Metadata
  - entity: track
    effect: reads
    facts:
    - Playback source
  contexts:
    main:
      place: desktop::lyrics-search
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/display_coordinator.py#DisplayCoordinator.current_lyrics_status
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_status.py
---

# Distinguish playback and lyric sources

## Trigger

The listener inspects current source status in Lyrics search.

## Outcome

Provider, acquisition, playback source, and cache state are reported separately; status refreshes when searches or applications complete.
