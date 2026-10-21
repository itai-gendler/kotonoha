---
appliesTo:
- type: entity
  id: lyrics
- type: entity
  id: track
references:
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/match.py#evaluate_match
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/match.py#ranked_matches
---

# Automatic matching preserves recording-version identity

Lyric-changing version conflicts are rejected. Conflicting known performers are rejected. Remaster-like lyric-neutral tags do not create a conflict. Exact title and artist identity can establish high confidence with up to eight seconds of duration discrepancy; weaker corroborated title matches use tighter duration evidence.
