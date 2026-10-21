---
kind: edge
routes:
  main: Main
steps:
- text: Cached lyrics cannot be restored as timed content.
  kind: condition
  entities:
  - entity: cached-lyrics
    effect: reads
    facts:
    - Content
  contexts:
    main:
      place: desktop::local-lyrics-cache
  unattended: true
- text: The Product removes invalid Cached lyrics and dependent Manual selection records.
  kind: product
  entities:
  - entity: cached-lyrics
    effect: removes
  - entity: manual-selection
    effect: removes
    with: cached-lyrics
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

# Discard content that no longer yields timed lyrics

## Trigger

A cache lookup finds stored content that can no longer be read as timed lyrics.

## Outcome

The invalid record and its bindings are removed and the lookup proceeds as a miss.
