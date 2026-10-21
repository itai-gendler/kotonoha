---
kind: edge
routes:
  main: Main
steps:
- text: A completed lookup belongs to a previous Track.
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
- text: The Product discards that completed result without publishing it.
  kind: product
  entities: []
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_lyrics.py#MprisLyricsCoordinator._load_song
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/workflow.py#LyricsResolutionWorkflow.resolve
---

# Ignore a completed lookup for an older song

## Trigger

The song changes while a lyric lookup is pending.

## Outcome

The older result does not replace the active song’s display.
