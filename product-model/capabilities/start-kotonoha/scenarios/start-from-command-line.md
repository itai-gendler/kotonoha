---
kind: primary
routes:
  main: Main
steps:
- text: The listener launches Kotonoha.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: command-line
- text: The Product loads Settings and starts the overlay, tray, and available integrations.
  kind: product
  actor: listener
  entities:
  - entity: settings
    effect: reads
    facts:
    - UI language
    - Theme
    - Window appearance
    - Icons
    - Font
    - Text sizes
    - Panel
    - Panel opacity
    - Panel tint
    - Accent
    - Effects
    - Karaoke
    - Global lead
    - Translation
    - Context lines
    - Script
    - Interlude
    - Placement
    - Click-through
    - Player preference
    - Lyric sources
    - Display sources
    - Prefer best match
    - Fuzzy matching
    - Cache enabled
    - Cider token
    - Pending changes
  contexts:
    main:
      place: command-line
references:
- kind: code
  role: implementation
  target: src/kotonoha/main.py#entry_point
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController.start
---

# Start from command line

## Trigger

The listener launches Kotonoha.

## Outcome

The overlay and tray are available, waiting for music or following an available source.

## Edge cases

- A second launch exits without adding another overlay or tray icon.
- A missing MPRIS session bus, an unreachable Cider, or an adapter port already in use does not stop the other integrations.
