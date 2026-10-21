---
type: cli
actors:
- listener
entryPoints:
- cli: kotonoha
references:
- kind: code
  role: implementation
  target: src/kotonoha/main.py#entry_point
---

# Command line

Start Kotonoha with an optional receiver-port override and diagnostic logging preference.
