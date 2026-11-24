# WaterHawk User Manual

Welcome to WaterHawk — an accessible, screen-reader-first editor for the Line 6
Firehawk FX, with a built-in suite of practice tools. This manual is written for
keyboard and screen-reader use throughout: every feature described here works without a
mouse and announces itself. It is structured with heading levels, so you can navigate it
the same way you navigate the app — by jumping between headings.

A note on what works today: **everything in this manual works right now except live
pedal control**, which is in its final validation stage. Tone editing, presets, the
and the tuner are fully functional offline. See
"The pedal connection" near the end for the current state of live control.

## Getting started

### What you need

- Windows, with Python 3.10 or newer installed.
- If you use a screen reader, WaterHawk is built and tested with **NVDA**. Spoken
  feedback also works through Windows speech when NVDA isn't running.
- Optionally: your Firehawk FX paired over Bluetooth (for the play-along feature now,
  and live control later).

### Installing

From the project folder, in a terminal:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -e ".[ui,dev]"
```

### First run: your tone data

WaterHawk ships none of Line 6's data. You generate it once, locally, from a copy of
the discontinued Firehawk Remote app (an APK file) that you lawfully have:

```powershell
.venv\Scripts\python tools\extract_assets.py path\to\firehawk-remote.apk
```

This fills in the 261 amp, cab, and effect models the editor works with. It only ever
lives on your machine.

### Launching

Double-click **`Firehawk.bat`**, or run `.venv\Scripts\python -m firehawk`.

**After updating the app's code, restart it** — a running copy keeps using the code it
launched with.

## The main window

The window is a list of tabs down the left side, with each tab's controls to the right.
The tabs are: **Presets**, one tab per signal-chain block (Wah, Compressor, Noise Gate,
Amp, Cabinet, EQ, FX 1–3, Reverb, Volume Pedal, Variax, Global), and the **Tuner**.

### Moving around

- **Up/Down arrows** on the tab list move between tabs; **Tab** moves into a tab's
  controls; **Escape** steps back out (controls → tab list → Presets).
- **Ctrl+1 through Ctrl+9** jump straight to the first nine tabs; **Ctrl+B** returns to
  Presets from anywhere.
- **F1** opens the complete keyboard-command list at any time.
- **Alt** opens the menus: File, Go, Settings, Device, Help.

### Making it yours

- **Settings → Arrange Tabs…** reorders the tabs: select one, press **Alt+Up** or
  **Alt+Down** to move it, OK to apply. The order persists between sessions. The first
  tab is where the app starts, and Ctrl+1–9 follow your order.
- **Settings → Dark Mode** toggles the high-contrast dark theme with large white labels
  (on by default).

## Presets and tone editing

### The Presets tab

A list of every preset — factory and your own — with a details pane that reads the
selected preset's full signal chain. From here you can **Open** a preset into the
editor, **Save Current As…**, **Delete**, and **Refresh**.

### Editing a tone

Each block tab (Amp, Reverb, FX 1, …) has:

- an **enabled checkbox** to switch the block on or off,
- a **model dropdown** to choose which amp/effect the block runs,
- one labelled control per parameter: **sliders** for continuous values (they announce
  real values — decibels, BPM, percent — not raw positions), **dropdowns** for stepped
  choices, **checkboxes** for switches.

Changing the model rebuilds the parameter list for the new model. All names and ranges
come from the pedal's own data — nothing is approximated.

### Saving and files

- **Ctrl+N** — new preset. **Ctrl+S** — save to your library (you'll be asked for a
  name). **Ctrl+O** — open a preset file. **File → Export Preset to File…** writes the
  current tone as a JSON file you can back up or share.
- If you have unsaved changes, the app offers Save / Discard / Cancel before anything
  would overwrite them.
- **Settings → User Presets Folder…** tells you where your library lives on disk.

## The Tuner

Tune by ear against a sustained reference tone — no lights, no meters.

1. Pick your **instrument**: 6, 7, or 8-string guitar, or 4, 5, or 6-string bass.
2. Pick a **tuning** — from standard through drop tunings, open tunings, DADGAD,
   all-fourths, and more.
3. Press a **string button** to hold that string's tone; tune to it; press again (or
   **Stop Tone**) to stop. The tone also stops when you leave the tab.

## Playing along with music

The Firehawk FX is also a Bluetooth speaker. Pair it with Windows, set it as the
playback device in Windows Sound settings, and any music you play comes through the
pedal while you play guitar over it. No app setting needed — see **Help → Playing Along
with Music** for the steps.

## The pedal connection

Live control — sending your edits to the pedal — is the one feature still in
validation. The protocol has been fully reverse-engineered and implemented; two final
byte-level details await confirmation against a capture of the original app's traffic.
Until then:

- **Device → Connect to Pedal…** finds the pedal's Bluetooth COM port.
- **Device → View Outgoing Messages…** shows the exact bytes each edit would send.
- **Transmit is off by default** and warns before enabling — nothing is written to
  your hardware until the protocol is confirmed safe.

Everything else in this manual is fully usable offline, today.

## Keyboard reference

| Keys | Action |
|------|--------|
| Ctrl+N / Ctrl+O / Ctrl+S | New / open / save preset |
| Ctrl+1 … Ctrl+9 | Jump to the first nine tabs (your order) |
| Ctrl+B | Back to Presets |
| Escape | Step back: controls → tab list → Presets; closes dialogs |
| Tab / Shift+Tab | Move between controls |
| Alt | Open the menus |
| F1 | Keyboard-command list (in the Pattern Editor: speaks the grid keys) |
| Alt+Up / Alt+Down | Move a tab (in Settings → Arrange Tabs) |

In the Pattern Editor grid: Up/Down lines · Left/Right step · Ctrl+Left/Right beat ·
Ctrl+Shift+Left/Right bar · Home/End · Space cycle on/accent/ghost/off · minus/plus line length (polymeter) ·
brackets `[`/`]` tune the line (Shift = octave) · comma/period `,`/`.` line volume · C choke group · Enter sample options · Delete remove line · P preview (speaks the note).

## Troubleshooting

- **A button seems to do nothing** — it should never happen (everything speaks); if it
  does, report it. Make sure you restarted the app after an update.
- **No tuner sound** — check Windows' output device and volume mixer;
  the app plays through the default output device.
- **Spoken grid navigation is silent** — the `accessible_output2` package provides
  direct speech; reinstall dependencies with
  `.venv\Scripts\python -m pip install -e ".[ui]"`.
- **The Groove dropdown doesn't show my edited pattern's name** — after editing, your
  working pattern is what plays even though the dropdown still names the last selected
  groove. Save it as a preset to give it a name in the list.

## Getting help and contributing

WaterHawk is free software:
[github.com/CoveCathedral/WaterHawk](https://github.com/CoveCathedral/WaterHawk).
Issues and pull requests are welcome — screen-reader testing feedback most of all.

**Licensing.** Copyright © 2026 Kaylea Fox, under the GNU Affero General Public License v3
or later. **You may use WaterHawk for anything, including paid work.** If you distribute a
modified version, you must share your source under the same license and keep the credit. For
closed-source or commercial use, a separate commercial license can be arranged — get in
touch. WaterHawk ships none of Line 6's data; you generate that locally from an app copy
you lawfully own.
