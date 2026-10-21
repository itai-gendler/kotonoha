---
references:
- kind: code
  role: implementation
  target: src/kotonoha/players.py#PlayerInfo
- kind: code
  role: implementation
  target: src/kotonoha/providers/player_selection.py#PlayerSelector
---

# Player

An MPRIS player instance offered by Sources and considered for playback selection.

## Information kept

- **Name** — The identity of a discovered MPRIS player.
- **Track metadata** — Its reported title and artist.
- **Playback status** — Its current playing, paused, stopped, or unknown status.
- **Current** — Whether the selection policy would follow this player.
