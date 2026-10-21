---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/resolver.py#LyricsResolver
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/workflow.py#LyricsResolutionWorkflow
- kind: code
  role: implementation
  target: src/kotonoha/providers/mpris_lyrics.py#MprisLyricsCoordinator
domain: sources
---

# Resolve lyrics

Find a complete timed lyric document for the active recording, restoring an explicit choice first and then following exact hints or configured automatic sources.
