---
availability:
- place: desktop
references:
- kind: doc
  role: intent
  target: README.md
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/dialog.py#SettingsDialog.current_config
- kind: code
  role: implementation
  target: src/kotonoha/app/config_service.py#ConfigService.apply_settings
- kind: code
  role: implementation
  target: src/kotonoha/app/services.py#RuntimeConfigApplier.apply
domain: sources
---

# Change Sources settings

Choose a preferred player, order and enable lyric providers and display sources, select best-match or ordered fallback, configure fuzzy matching and caching, and supply an optional Cider API token.
