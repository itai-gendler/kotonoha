---
kind: edge
routes:
  main: Main
steps:
- text: The active Track needs lyric resolution.
  kind: condition
  entities:
  - entity: track
    effect: reads
    facts:
    - Title
    - Artist
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product begins resolving the Track.
  kind: product
  entities:
  - entity: track
    effect: changes
    from: Detected
    to: Resolving
    facts:
    - Lyric status
  contexts:
    main:
      place: desktop::overlay
- text: The Product records that no timed document was found for the Track.
  kind: product
  entities:
  - entity: track
    effect: changes
    from: Resolving
    to: Lyrics not found
    facts:
    - Lyric status
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/workflow.py#LyricsResolutionWorkflow
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_lyrics.py#MprisLyricsCoordinator
---

# Finish with no timed lyrics

## Trigger

All eligible sources miss or fail.

## Outcome

The song remains visible as title and artist with no stale lyric document.

## Edge cases

- Ordinary provider misses are remembered briefly in memory; transport failures are not remembered as misses.
- Cache lookup failure allows the same provider’s network lookup to proceed.
