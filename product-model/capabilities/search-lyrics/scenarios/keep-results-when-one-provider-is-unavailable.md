---
kind: edge
routes:
  main: Main
steps:
- text: The listener searches for lyric candidates.
  kind: actor
  actor: listener
  entities: []
  contexts:
    main:
      place: desktop::lyrics-search
- text: The Product presents available Lyrics and reports the unavailable source.
  kind: product
  actor: listener
  entities:
  - entity: lyrics
    effect: creates
    facts:
    - Provider
    - Song identity
    - Metadata
    - Timed text
    - Timing
    - Confidence
    - Acquisition
    - Cache state
  contexts:
    main:
      place: desktop::lyrics-search
references:
- kind: code
  role: implementation
  target: src/kotonoha/lyrics/search.py#LyricsSearchService.search
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_dialog.py#LyricsSearchDialog.set_results
- kind: code
  role: implementation
  target: src/kotonoha/ui/settings/lyrics_search_model.py#LyricsSearchSortModel
---

# Keep results when one provider is unavailable

## Trigger

One configured provider times out, fails, rejects its payload, or does not support metadata search.

## Outcome

Other providers’ candidates remain usable, with an unavailable-source reason for the unsuccessful provider.

## Edge cases

- QQ Music, Cider, and unconfigured sources have explicit unavailable reasons rather than pretending to search.
- A completed search with no candidates displays an empty result.
