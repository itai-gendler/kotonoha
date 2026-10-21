---
kind: primary
routes:
  main: Main
steps:
- text: The listener requests Settings.
  kind: actor
  actor: listener
  entities:
  - entity: settings
    effect: reads
    facts: []
  contexts:
    main:
      place: desktop::overlay
- text: The Product stages the current Settings and opens General.
  kind: product
  actor: listener
  entities:
  - entity: settings
    effect: changes
    facts:
    - Pending changes
  contexts:
    main:
      place: desktop::general
references:
- kind: code
  role: implementation
  target: src/kotonoha/app/application_controller.py#AppController._open_settings_async
---

# Open current preferences

## Trigger

The listener opens Settings.

## Outcome

The listener arrives at General with a staged configuration; discovered players are available under Sources.

## Edge cases

- Opening an existing Settings window focuses it without replacing its pending edits.
- Player discovery failure leaves Settings usable with an empty discovered-player list.
