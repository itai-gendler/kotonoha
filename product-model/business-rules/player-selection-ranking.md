---
appliesTo:
- type: entity
  id: player
- type: entity
  id: settings
  facts:
  - Player preference
references:
- kind: code
  role: implementation
  target: src/kotonoha/providers/player_selection.py#PlayerSelector
---

# A preferred eligible player wins before automatic ranking

Playing and paused players are eligible. An eligible preferred player wins, including when paused. Automatic playing candidates rank performer metadata before recency, then title and continuity. A paused song beats a playing instance without a song. An unavailable preference does not disable fallback.
