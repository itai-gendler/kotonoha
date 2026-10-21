---
appliesTo:
- type: entity
  id: track
  effect: creates
  contexts:
  - place: adapter
references:
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#_is_local_origin
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver
permits:
- actors:
  - external-adapter
  when:
  - entity: external-adapter
    fact: Connection origin
    is: Local
---

# Local external adapters can publish track snapshots

Only adapters connecting from this computer are accepted. What they publish is shown only when the display-source order gives that adapter the playback.
