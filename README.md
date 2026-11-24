# FreedomHawk

**An open-source, accessible, screen-reader-first Windows controller for the Line 6 Firehawk FX.**

## Why this project exists

I own a Firehawk FX. Line 6 discontinued the Firehawk Remote app in 2024. Its only
editor was a mobile app that was never built to be accessible, and it depends on a cloud
login layer that is fading. The pedal has six knobs and a tiny screen, so a blind or
low-vision owner cannot reach hundreds of parameters (amps, cabs, effects, reverbs, wah).

To keep using my pedal, I was obligated to rework it, using a form that suits my needs.
That is the same path every Firehawk owner who needs an accessible editor is forced to take.
FreedomHawk gives that option to more users: a free, open editor for the hardware you already own.

## Status

This is early, working software. It is not affiliated with or endorsed by Line 6.

- Reads the tone model: 261 amps, cabs, effects, and reverbs with their parameters and ranges.
- Edits every block with native, labelled controls (checkboxes, sliders, dropdowns).
- Saves and opens presets on your computer.
- Tuner with reference tones and tuning library.
- Pedal link: the wire protocol is documented in `docs/protocol.md`. Live transmit to the
  pedal stays gated and off by default until it is validated against a real capture.

## Accessibility

- Native Windows controls only, so NVDA reads labels, values, and ranges correctly.
- Keyboard-first: every control is reachable without a mouse.
- High-contrast dark mode by default, with large labels for low-vision use.
- An HTML user manual opened from Help.

## Your tone data is not included

FreedomHawk ships **no** Line 6 data. You generate it once from an APK of the (discontinued)
Firehawk Remote app that you lawfully have. This keeps the project a clean interoperability
tool that redistributes nothing proprietary. See `src/firehawk/data/README.md`.

## How this project was built (AI disclosure)

This is my first fully agentic-coded software. I use **pi** (the pi coding agent) as the
harness for AI-assisted development. I am learning how to work well with AI: writing
better prompts and skills, deciding what to delegate, and checking the results.

My goal is to use AI to augment my workflow without giving up learning. I want to
understand the core parts of this code (the protocol, the model, the accessibility rules)
even when I do not type them myself. Reviews, tests, and decisions are mine; the code is a
collaboration with AI agents, and it is verified by running it, not by trusting it.

If you find a bug or an accessibility problem, please open an issue. Screen-reader
feedback from real NVDA use is especially valuable.

## Setup

Requires Windows and Python 3.10 or newer (developed on 3.12).

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -e ".[ui,dev]"
```

Generate your tone data (see above), then run:

```powershell
.venv\Scripts\python tools\extract_assets.py path\to\firehawk-remote.apk
.venv\Scripts\python -m firehawk
```

Or double-click `Firehawk.bat`. To run the tests:

```powershell
.venv\Scripts\python -m pytest
```

## Project layout

```
src/firehawk/
  model/      tone model: models, parameters, ranges, value types
  protocol/   wire format: CRC-16, frames, addressing (pure, unit-tested)
  transport/  serial port and offline simulator
  device/     gated bridge from edits to the pedal (transmit off by default)
  tuner/      tone generator and tuning library
  ui/         wxPython interface
docs/         protocol notes, user manual, decisions, roadmap status
tools/        extract_assets.py and reverse-engineering helpers
tests/        pytest suite
```

## Contributing

Open an issue first so we can agree on the scope. `scripts/gate.py` must pass before a
change is proposed.

## License

AGPL-3.0-or-later. See `LICENSE`.
