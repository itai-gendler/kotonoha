---
availability:
- place: adapter
references:
- kind: doc
  role: intent
  target: plugins/README.md
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver._drop_client
---

# Disconnect an adapter

End an external adapter session and release its retained playback candidate.
