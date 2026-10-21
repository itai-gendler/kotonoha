---
kind: alternate
routes:
  main: Main
steps:
- text: The Track metadata does not describe a supported single-song lookup.
  kind: condition
  entities:
  - entity: track
    effect: reads
    facts:
    - Title
    - Duration
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product records no lyric result for the Track.
  kind: product
  entities:
  - entity: track
    effect: changes
    from: Detected
    to: Lyrics not found
    facts:
    - Lyric status
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_track.py#lyrics_lookup_reason
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_resolution.py#MprisResolutionSession.resolve
---

# Skip a non-song upload

## Trigger

Playback metadata describes an upload treated as a compilation, concert, medley, or an over-two-hour item.

## Outcome

Automatic lyric lookup is skipped and the overlay retains song metadata as fallback.

## Edge cases

- A duration detected as cumulative session playtime is treated as unknown, allowing ordinary single-song lookup.
- A matching live source can provide the trusted duration instead of MPRIS.
