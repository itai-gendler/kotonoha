---
appliesTo:
- type: entity
  id: lyrics
  effect: creates
  contexts:
  - place: adapter
references:
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/protocol.py#AdapterProtocolDecoder
permits:
- actors:
  - external-adapter
  when:
  - entity: external-adapter
    fact: Connection origin
    is: Local
---

# Local external adapters can publish complete lyrics

The local adapter contract accepts complete lyric documents; the product derives current lines and progress from source data.
