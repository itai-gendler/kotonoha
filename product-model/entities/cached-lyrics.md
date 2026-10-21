---
relations:
- entity: manual-selection
  verb: supports
  cardinality: one-to-many
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage
---

# Cached lyrics

Persistent lyric content addressed by provider and song identity, browsed and deleted in Local lyrics cache.

## Information kept

- **Provider** — The lyric provider owning the record.
- **Song identity** — The provider-scoped song identity.
- **Title** — The provider title.
- **Artist** — The provider performer.
- **Album** — The provider album.
- **Duration** — The provider duration when available.
- **Content** — The original lyric payload from which timed lines can be recovered.
- **Mode** — AUTO or MANUAL as recorded for the content.
- **Fetched at** — When content was stored.
- **Last used** — When content was last stored or successfully restored.
