---
appliesTo:
- type: entity
  id: timing-correction
- type: entity
  id: settings
  facts:
  - Global lead
references:
- kind: code
  role: implementation
  target: src/kotonoha/display/offsets.py#clamp_track_offset
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/content.py#OverlayContentController
- kind: code
  role: implementation
  target: src/kotonoha/display/presentation.py#DisplayEngine._display_position
---

# Timing corrections are bounded and added to the global lead

Each earlier action adds 100 ms; each later action subtracts 100 ms. Corrections clamp to ±10 seconds. Display time is playback time plus the global lead and version-specific correction; source timestamps remain unchanged.
