---
appliesTo:
- type: capability
  id: publish-snapshot
- type: capability
  id: calibrate-playback
- type: entity
  id: external-adapter
references:
- kind: doc
  role: intent
  target: plugins/README.md
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver.ingest
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver._publish_clock
---

# Accepted adapter messages advance one connection sequence

Snapshots and clocks share a strictly increasing accepted sequence per connection. A clock refers to that connection’s latest accepted snapshot. Reconnection starts a new sequence space and supplies a complete snapshot.
