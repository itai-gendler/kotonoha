---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: README.md
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/app/lyrics_search.py#LyricsSearchController._apply_async
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/cache/storage.py#LyricsCacheStorage.select
- kind: code
  role: implementation
  target: src/kotonoha/app/display_coordinator.py#DisplayCoordinator.apply_manual_artifact
---

# Apply lyrics

Persist a chosen search result as a manual selection for the original playback identity, then apply it immediately when the active song still matches.
