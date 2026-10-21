---
kind: primary
routes:
  main: Main
steps:
- text: The listener cancels Settings.
  kind: actor
  actor: listener
  entities:
  - entity: settings
    effect: reads
    facts: []
  contexts:
    main:
      place: desktop::general
- text: The Product discards pending Settings edits and closes the window.
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
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog
---

# Discard unapplied settings

## Trigger

The listener closes or cancels Settings after making pending edits.

## Outcome

Applied preferences remain; unapplied edits are discarded.

## Edge cases

- OK applies pending changes before closing; Cancel does not undo an earlier Apply.
