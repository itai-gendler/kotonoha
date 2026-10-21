---
kind: alternate
routes:
  main: Main
steps:
- text: There is no active song.
  kind: condition
  entities: []
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product displays the idle indication.
  kind: product
  entities: []
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/display/presentation.py#DisplayEngine
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/content.py#OverlayContentController
---

# Wait for music without a track

## Trigger

No active song is available.

## Outcome

The overlay shows the waiting-for-music state without old lyrics.
