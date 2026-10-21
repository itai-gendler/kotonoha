---
kind: primary
routes:
  main: Main
steps:
- text: The automatic cache exceeds its capacity.
  kind: condition
  entities:
  - entity: cached-lyrics
    effect: reads
    facts:
    - Mode
    - Last used
  contexts:
    main:
      place: desktop::local-lyrics-cache
  unattended: true
- text: The Product removes the least-recently-used eligible Cached lyrics.
  kind: product
  entities:
  - entity: cached-lyrics
    effect: removes
  contexts:
    main:
      place: desktop::local-lyrics-cache
references:
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage._write
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage._read_hit
---

# Remove least-recently-used automatic content

## Trigger

A content write exceeds the automatic cache capacity.

## Outcome

The oldest eligible automatic records are removed until the default 1,000-entry automatic limit is met. Manual and previously bound content is retained.
