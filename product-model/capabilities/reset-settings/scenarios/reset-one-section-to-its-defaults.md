---
kind: primary
routes:
  general: General
  icon: Icon
  text: Text
  panel: Panel
  effects: Effects
  lyrics: Lyrics
  position: Position
  sources: Sources
steps:
- text: The listener chooses Reset on the open section.
  kind: actor
  actor: listener
  entities: []
  contexts:
    general:
      place: desktop::general
    icon:
      place: desktop::icon
    text:
      place: desktop::text
    panel:
      place: desktop::panel
    effects:
      place: desktop::effects
    lyrics:
      place: desktop::lyrics
    position:
      place: desktop::position
    sources:
      place: desktop::sources
- text: The Product returns that section's pending Settings values to their defaults.
  kind: product
  actor: listener
  entities:
  - entity: settings
    effect: changes
    facts:
    - Pending changes
  contexts:
    general:
      place: desktop::general
    icon:
      place: desktop::icon
    text:
      place: desktop::text
    panel:
      place: desktop::panel
    effects:
      place: desktop::effects
    lyrics:
      place: desktop::lyrics
    position:
      place: desktop::position
    sources:
      place: desktop::sources
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/form_state.py#SettingsFormState.reset_page
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog._reset_current_page
---

# Reset one section to its defaults

## Trigger

The listener chooses Reset on one Settings section: General, Icon, Text, Panel, Effects, Lyrics, Position or Sources.

## Outcome

Only that section's pending values return to their defaults; other sections keep their pending edits. Nothing changes until Apply or OK.

## Edge cases

- Cancel or closing Settings discards the reset along with any other pending edits.
