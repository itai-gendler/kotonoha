---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: README.md
- kind: code
  role: implementation
  target: src/kotonoha/ui/overlay/window.py#LyricsOverlay.mousePressEvent
- kind: code
  role: implementation
  target: src/kotonoha/platform/qt_window.py
domain: position
---

# Request the system window menu

Ask a supported ordinary desktop window for its compositor-owned menu, including available stacking controls.
