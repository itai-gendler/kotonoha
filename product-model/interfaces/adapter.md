---
type: api
actors:
- external-adapter
entryPoints:
- api: ws://127.0.0.1:28745/kotonoha/adapter
references:
- kind: doc
  role: intent
  target: plugins/README.md
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver
---

# External adapter protocol

Local integrations submit complete playback snapshots and clock calibrations. The product does not send application-level acknowledgements or resynchronization commands.
