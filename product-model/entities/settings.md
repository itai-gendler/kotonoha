---
singleton: true
references:
- kind: code
  role: implementation
  target: src/kotonoha/config/models.py#Config
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/form_state.py#SettingsFormState
---

# Settings

The listener’s configuration for this Kotonoha installation, plus pending edits while the Settings window is open.

## Information kept

- **UI language** — Automatic system language or English, Simplified Chinese, Traditional Chinese, or Japanese.
- **Theme** — Automatic, light, or dark appearance.
- **Window appearance** — Settings-window blur preference and opacity.
- **Icons** — Independent system-tray and window icon choices.
- **Font** — Lyric font family and style.
- **Text sizes** — Independent main, context, and translation sizes.
- **Panel** — Panel style, width mode, width, and long-line behavior.
- **Panel opacity** — Separate ordinary and frosted panel opacity preferences.
- **Panel tint** — Whether the panel follows the accent.
- **Accent** — The selected lyric accent colors.
- **Effects** — Animation, line transition, glow, word emphasis, and intensity preferences.
- **Karaoke** — Whether word timing is used for highlighting when present.
- **Global lead** — Display-wide timing lead, from minus two to plus two seconds.
- **Translation** — Whether available lyric translations are shown.
- **Context lines** — Whether previous and next lines accompany the current line.
- **Script** — Original, Simplified Chinese, or Traditional Chinese display conversion.
- **Interlude** — The marker and optional countdown used during instrumental gaps.
- **Placement** — Top or bottom anchoring, edge margin, and horizontal offset.
- **Click-through** — Whether the overlay passes pointer input through.
- **Player preference** — Automatic selection or a preferred MPRIS player instance.
- **Lyric sources** — Enabled lyric providers in priority order.
- **Display sources** — Enabled playback sources in priority order.
- **Prefer best match** — Whether match confidence or strict provider order decides automatic resolution.
- **Fuzzy matching** — Whether noisy title recovery widens provider queries and acceptance.
- **Cache enabled** — Whether automatic lyric cache reads and writes, including manual restoration, are enabled.
- **Cider token** — The optional credential supplied to the local Cider API.
- **Pending changes** — Values staged in the open Settings form until applied or discarded.
- **Saved output** — The display output, and its size, on which the last successful overlay move was measured.
