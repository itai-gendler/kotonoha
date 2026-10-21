---
references:
- kind: code
  role: implementation
  target: src/kotonoha/playback/models.py#TrackIdentity
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_lyrics.py#MprisLyricsCoordinator
---

# Track

A recording currently followed or retained as a source candidate. Resolution state is independent of whether playback is paused.

## Information kept

- **Title** — The normalized playback title.
- **Artist** — The performer reported or recovered from player metadata.
- **Album** — The playback album when available.
- **Duration** — The trusted duration when known.
- **Playback source** — The player integration supplying active playback facts.
- **Playback status** — Playing, paused, stopped, or unknown.
- **Position** — The current playback time when available.
- **Lyric status** — Whether lyric resolution is pending, available, or not found.
- **Identity** — The player and recording identity used to distinguish track changes.

## States

### Detected

Playback facts identify a recording.

### Resolving

A lyric lookup for this recording is in progress.

### Lyrics available

A complete timed document has been selected for this recording.

### Lyrics not found

The completed resolution has no usable timed document.
