---
appliesTo:
- type: entity
  id: settings
  facts:
  - Lyric sources
  - Display sources
references:
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/sources.py#SettingsSourcesPageBuilder._keep_one_source_checked
- kind: code
  role: implementation
  target: src/kotonoha/config/models.py#Config.clamped
---

# Each source list retains at least one enabled entry

Lyric and display source lists are independently ordered and nonempty. The settings form rechecks the first row if the last checked entry is cleared; loaded invalid or empty lists use the corresponding defaults.
