---
appliesTo:
- type: entity
  id: track
  effect: creates
  contexts:
  - place: desktop
permits:
- unattended: true
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/display_coordinator.py#DisplayCoordinator
---

# Only Kotonoha's own playback discovery starts a desktop track

A track on the desktop begins when Kotonoha observes playback. The listener never creates one directly: manual lyric search works on the track already followed.
