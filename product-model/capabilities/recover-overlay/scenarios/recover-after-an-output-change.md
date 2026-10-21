---
kind: primary
routes:
  main: Main
steps:
- text: The current output disappears.
  kind: condition
  entities: []
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product chooses an available output and reapplies Settings presentation.
  kind: product
  entities:
  - entity: settings
    effect: reads
    facts:
    - Placement
    - Click-through
    - Panel
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/surface.py#OverlaySurfaceController.screen_removed
- kind: code
  role: implementation
  target: src/kotonoha/platform/surface_lifecycle.py#SurfaceLifecycleOwner
---

# Recover after an output change

## Trigger

The output hosting the overlay is removed.

## Outcome

The overlay attempts to bind to a remaining output and reapplies presentation and input behavior after a successful rebuild.

## Edge cases

- If no output is available, recovery waits until an output becomes available.
- Retryable surface failures are retried by the lifecycle owner.
