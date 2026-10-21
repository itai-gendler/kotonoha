---
kind: primary
routes:
  main: Main
steps:
- text: The Track and Lyrics identify a saved Timing correction.
  kind: condition
  entities:
  - entity: track
    effect: reads
    facts:
    - Title
    - Artist
    - Album
    - Duration
  - entity: lyrics
    effect: reads
    facts:
    - Provider
    - Song identity
    - Timed text
  - entity: timing-correction
    effect: reads
    facts:
    - Recording
    - Lyric version
    - Correction
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product projects Lyrics using the Timing correction and Settings global lead.
  kind: product
  entities:
  - entity: lyrics
    effect: reads
    facts:
    - Timed text
  - entity: timing-correction
    effect: reads
    facts:
    - Correction
  - entity: settings
    effect: reads
    facts:
    - Global lead
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/state/track_offset_store.py#TrackOffsetStore.load
- kind: code
  role: implementation
  target: src/kotonoha/display/presentation.py#DisplayEngine._display_position
---

# Restore the exact lyric version’s correction

## Trigger

A displayed recording and lyric document identify an existing correction.

## Outcome

The saved correction is added to the global lead when deriving display time. Changing cache/manual origin alone preserves the correction identity.

## Edge cases

- A different provider, lyric content, timing, or translation has a different correction identity.
- A recording with no saved correction uses zero per-version adjustment.
- The older structured duration format is migrated to whole seconds; legacy configuration-string offsets are ignored.
