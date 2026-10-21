---
appliesTo:
- type: entity
  id: lyrics
  effect: creates
  contexts:
  - place: desktop
- type: entity
  id: lyrics
  effect: changes
  contexts:
  - place: desktop
- type: entity
  id: track
  effect: changes
  contexts:
  - place: desktop
permits:
- actors:
  - listener
- unattended: true
references:
- kind: doc
  role: intent
  target: docs/SPEC.md
- kind: code
  role: implementation
  target: src/kotonoha/app/display_coordinator.py#DisplayCoordinator
---

# On the desktop, only the listener and Kotonoha itself change the track and its lyrics

Kotonoha follows playback and resolves lyrics on its own; the listener changes them by searching for and applying lyrics. There is no account, sign-in or administrator role.
