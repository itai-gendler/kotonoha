---
scope: Core desktop, launch, playback and lyric resolution, manual selection, timing state, cache management, and
  external adapter ingress.
method: Static source tracing from the English README and specifications through UI, application, provider, and
  persistence boundaries; selected tests read as supporting evidence.
covered:
- description: Application controllers, source arbitration, configuration application, search and cache workflows.
  paths:
  - src/kotonoha/app/
- description: MPRIS selection, stable track commits, resolution ownership, and Cider polling.
  paths:
  - src/kotonoha/providers/
  - src/kotonoha/playback/
- description: Lyric resolution, matching policy, local sources, source contracts, search and cache persistence.
  paths:
  - src/kotonoha/lyrics/resolver.py
  - src/kotonoha/lyrics/workflow.py
  - src/kotonoha/lyrics/match.py
  - src/kotonoha/lyrics/sources.py
  - src/kotonoha/lyrics/local.py
  - src/kotonoha/lyrics/catalog.py
  - src/kotonoha/lyrics/search.py
  - src/kotonoha/lyrics/search_policy.py
  - src/kotonoha/lyrics/cache/
  - src/kotonoha/lyrics/adapter.py
  - src/kotonoha/lyrics/artifact.py
  - src/kotonoha/lyrics/hint.py
  - src/kotonoha/lyrics/live_contracts.py
  - src/kotonoha/lyrics/live_source.py
  - src/kotonoha/lyrics/models.py
  - src/kotonoha/lyrics/network_sources.py
  - src/kotonoha/lyrics/payload.py
  - src/kotonoha/lyrics/http.py
  - src/kotonoha/lyrics/__init__.py
- description: Display projection, gap detection, media-time interpolation and version-specific timing offsets.
  paths:
  - src/kotonoha/display/
  - src/kotonoha/clock.py
  - src/kotonoha/state/
  - src/kotonoha/lyrics/hanzi_fold.py
- description: Desktop overlay, settings sections, search and cache dialogs, tray and interface language catalog.
  paths:
  - src/kotonoha/ui/
  - src/kotonoha/tray.py
  - src/kotonoha/strings/
  - src/kotonoha/players.py
- description: Configuration loading, staged preference merging and persistence.
  paths:
  - src/kotonoha/config/
- description: Launch and adapter ingress contracts.
  paths:
  - src/kotonoha/main.py
  - src/kotonoha/__main__.py
  - src/kotonoha/__init__.py
  - src/kotonoha/receiver.py
  - src/kotonoha/lyrics/protocol.py
- description: Platform selection, movement, ordinary-window fallback and output recovery contract.
  paths:
  - src/kotonoha/platform/window_platform.py
  - src/kotonoha/platform/qt_window.py
  - src/kotonoha/platform/surface_lifecycle.py
  - src/kotonoha/platform/restart.py
  - src/kotonoha/platform/__init__.py
  - src/kotonoha/platform/detect.py
  - src/kotonoha/platform/overlay_contracts.py
  - src/kotonoha/platform/qt_host.py
exclusions:
- description: Build and release automation, packaging recipes and CI; engineering delivery rather than listener
    behavior.
  paths:
  - scripts/
  - packaging/
  - .github/
  - CMakeLists.txt
  - flake.nix
  - src/kotonoha/build_bridge.sh
  - uv.lock
  - pyproject.toml
  - flake.lock
- description: Visual assets, drawing primitives and screenshot content; design rather than product meaning.
  paths:
  - src/kotonoha/assets/
  - src/kotonoha/icons.py
  - src/kotonoha/leaf_icon.py
  - screenshots/
- description: Test harnesses and corpora; evidence rather than supported interfaces.
  paths:
  - tests/
- description: Worker, task and file-read plumbing; internal execution mechanisms.
  paths:
  - src/kotonoha/async_worker.py
  - src/kotonoha/async_task.py
  - src/kotonoha/file_access.py
unmapped:
- description: Individual provider query endpoints, retry budgets and format-specific parser edge cases; bounded
    to source contracts in this initial model.
  paths:
  - src/kotonoha/lyrics/netease.py
  - src/kotonoha/lyrics/qqmusic.py
  - src/kotonoha/lyrics/lrclib.py
  - src/kotonoha/lyrics/kugou.py
  - src/kotonoha/lyrics/lrc_parser.py
  - src/kotonoha/lyrics/yrc_parser.py
  - src/kotonoha/lyrics/krc_parser.py
  - src/kotonoha/lyrics/cider_api.py
- description: Exhaustive language-specific title, artist, version and browser-upload grammar; only shared recording-match
    policy is modeled.
  paths:
  - src/kotonoha/lyrics/title_grammar.py
  - src/kotonoha/lyrics/artist_grammar.py
  - src/kotonoha/lyrics/version_grammar.py
  - src/kotonoha/lyrics/player_title_grammar.py
  - src/kotonoha/lyrics/title_queries.py
- description: Configuration-file-only translation-language selection and every locale mapping; UI language and
    translation visibility are covered.
  paths:
  - src/kotonoha/i18n.py
  - src/kotonoha/lyrics/translation.py
- description: Native bridge ABI probing, detailed compositor protocol negotiation and full recovery retry matrix;
    observable fallback and movement are covered.
  paths:
  - src/kotonoha/platform/native.py
  - src/kotonoha/platform/native_abi.py
  - src/kotonoha/platform/bridge_probe.py
  - src/kotonoha/platform/layer_shell.py
  - src/kotonoha/layer_shell_bridge.cpp
  - src/kotonoha/protocols/
limitations: []
---

# Coverage
