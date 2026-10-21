---
availability:
- place: adapter
references:
- kind: doc
  role: intent
  target: plugins/README.md
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver._publish_clock
- kind: code
  role: implementation
  target: src/kotonoha/display/timeline.py#TimelineEngine
---

# Calibrate playback

Send position and playback-status observations for the latest accepted adapter snapshot.
