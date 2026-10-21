---
acts: external
kind: system
references:
- kind: doc
  role: intent
  target: plugins/README.md
- kind: code
  role: implementation
  target: src/kotonoha/receiver.py#AdapterReceiver
---

# External adapter

An independently supplied integration that publishes normalized playback and complete lyric documents.

## Information kept

- **Connection origin** — The local adapter origin accepted by the receiver.
- **Connection** — Whether this adapter connection is present.
