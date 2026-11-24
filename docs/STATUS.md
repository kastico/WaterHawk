# WaterHawk — Status

**Slim by design.** The tracker is the source of truth — this is a summary plus a pointer,
refreshed at phase boundaries.

- **Live queue:** https://github.com/CoveCathedral/WaterHawk/issues
- **Fastest view:** `gh issue list` · **What waits on Kaylea:** `gh issue list --label needs-human-test`
- **Decisions:** [DECISIONS.md](DECISIONS.md) · **Full phase history:** [../ROADMAP.md](../ROADMAP.md)

## Where things stand (2026-07-20)

WaterHawk is an accessible, screen-reader-first Windows controller for the Line 6 Firehawk
FX pedal — the offline replacement for the discontinued Firehawk Remote app.

**Working today (offline):** the full tone model (261 models, ranges, types), the accessible
wxPython editor (native NVDA-readable controls only), local preset library, and an offline
transport. 116 tests pass.

**The one frontier:** live transmit to the pedal. The wire protocol is reverse-engineered
and implemented (CRC-16/CCITT-FALSE, the `0x55 0x55` frame, the ToneMatch command set,
symbol-table addressing) bar **two inferred constants** (float type tag, ToneMatch transport
port). Both fall out of **one Bluetooth HCI capture** of the old app changing a parameter —
blocked only on locating the pedal's power cord. Transmit is gated OFF until then.

**Milestones:** Phase 2 (transmit validation) · Phase 5 (live device features) · Phase 6
(hardening & release) · v2 Horizon.
