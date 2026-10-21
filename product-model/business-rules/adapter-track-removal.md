---
appliesTo:
- type: entity
  id: track
  effect: removes
  contexts:
  - place: adapter
permits:
- actors:
  - external-adapter
references:
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver._drop_client
---

# An external adapter's track is released when the adapter disconnects

Ending the connection releases the adapter's retained playback. The display changes only when that adapter owned what was shown.
