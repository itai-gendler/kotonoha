---
appliesTo:
- type: entity
  id: settings
  effect: changes
  contexts:
  - place: desktop::overlay
  facts:
  - Placement
  - Saved output
permits:
- actors:
  - listener
  when:
  - fact: Click-through
    is: false
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/window.py#LyricsOverlay.mousePressEvent
---

# The listener can move placement while the overlay is unlocked

Direct movement of the overlay requires pointer interaction. The Position form remains the preference-editing path.
