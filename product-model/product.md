---
id: kotonoha
summary: Synchronized desktop lyrics for Linux media players, with manual selection and lasting timing corrections.
category: music
tags:
- lyrics
- linux
- desktop
authors:
- name: Locez
license: MIT
languages:
- en
- zh-Hans
- zh-Hant
- ja
limitations:
- Music playback remains in the external player; Kotonoha follows its track and position.
- The desktop overlay targets Linux; fullscreen stacking and background blur depend on compositor support.
- Embedded audio-tag lyrics require the optional embedded-lyrics dependency.
- The local cache manager searches and deletes content; lyric replacement uses current-track search.
- Preferences, cached lyrics and timing corrections stay on this computer; there is no account or sync.
references:
- kind: doc
  role: intent
  target: README.md
- kind: doc
  role: intent
  target: docs/SPEC-lyrics.md
- kind: code
  role: implementation
  target: src/kotonoha/main.py#entry_point
---

# Kotonoha

Kotonoha is a Linux desktop lyrics overlay. It follows the current song and playback position, finds timed lyrics, and shows synchronized lines, word highlighting, and available translations. Listeners can choose a better lyric match, retain that choice, and correct the timing for an exact lyric version.

## Intent

The README describes Kotonoha as a “Linux desktop lyrics overlay” that works with MPRIS-compatible players without a player-specific plugin. Its purpose is to keep lyrics alongside the music people already play, with configurable sources, manual selection, and a desktop overlay they can position and personalize.
