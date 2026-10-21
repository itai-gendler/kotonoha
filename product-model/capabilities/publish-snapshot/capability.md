---
availability:
- place: adapter
references:
- kind: doc
  role: intent
  target: plugins/README.md
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver._publish_snapshot
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/protocol.py#AdapterProtocolDecoder
---

# Publish a playback snapshot

Publish complete normalized playback and an optional complete timed lyric document through the local adapter contract.
