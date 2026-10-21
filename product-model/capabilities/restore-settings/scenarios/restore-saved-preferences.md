---
kind: primary
routes:
  main: Main
steps:
- text: The application is loading its configuration.
  kind: condition
  entities: []
  contexts:
    main:
      place: desktop::overlay
  unattended: true
- text: The Product establishes Settings from saved preferences or defaults.
  kind: product
  entities:
  - entity: settings
    effect: creates
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
    - Saved output
  contexts:
    main:
      place: desktop::overlay
references:
- kind: code
  role: implementation
  target: src/kotonoha/config/store.py#ConfigStore.load
- kind: code
  role: implementation
  target: src/kotonoha/config/models.py#Config.from_dict
---

# Restore saved preferences

## Trigger

Kotonoha initializes its configuration.

## Outcome

Saved preferences are loaded and normalized before the desktop workflow uses them.

## Edge cases

- Unknown fields are ignored; known values are constrained to supported ranges.
- Unreadable or missing configuration uses defaults.
- Invalid JSON is set aside as a corrupt file when possible before defaults are used.
