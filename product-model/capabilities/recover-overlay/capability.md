---
availability:
- place: desktop
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/surface.py#OverlaySurfaceController.screen_removed
- kind: code
  role: implementation
  target: src/kotonoha/platform/surface_lifecycle.py#SurfaceLifecycleOwner
domain: position
---

# Recover the overlay

On platforms supporting output rebinding, rebind the overlay to an available output when its display disappears, and restore presentation after a successful surface rebuild.
