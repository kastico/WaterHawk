# WaterHawk — Decision Records

Numbered, append-only records: context, decision, consequences, and any standing
obligations. A deviation from plan requires a new record. Newest at the bottom.

---

## DR-001 — Adopt the agile + GitHub-tracker process (2026-07-20)

**Context.** WaterHawk reached real structure — a reverse-engineered wire protocol, an
accessible wxPython editor, an offline transport, 116 passing tests — but its backlog lived
in prose (`ROADMAP.md`, the working `THREADS.md`) and in memory. Kaylea runs an agile +
GitHub-native tracking process (proven on Silk; see
`C:\Users\Kaylie\.claude\PROCESS-PLAYBOOK.md`) and asked to bootstrap this project onto it.

**Decision.** Adopt the process, additively and forward-looking, per the playbook's
"Bootstrapping an existing project" recipe:

- **GitHub issues + milestones are the work queue.** Milestones map to the real ROADMAP
  phases (Phase 2 transmit validation, Phase 5 live device features, Phase 6 hardening) plus
  a "v2 Horizon" for unscheduled ideas. The prose backlog was captured as issues.
- **Records stay in the repo:** this file, plus a slim `docs/STATUS.md` that points at the
  tracker.
- **Reviews with teeth** once feature work resumes: two reviewers — code correctness and
  accessibility — each with veto, verdicts carried as `review:*` labels (GitHub refuses
  formal review states on same-account PRs). A local gate script (`scripts/gate.py`) must
  pass before any PR opens.
- **Agents carry identity trailers** (see `AGENTS.md`); one agent per working tree; isolated
  `git worktree` for concurrency; no concurrent full test gates.
- **Human checkpoints close sprints.** NVDA behavior is never claimed by an agent — it is
  enumerated for Kaylea to verify, and her recorded results outrank any agent's reasoning.

**Consequences.** From the next task onward, work flows through the tracker with
branch-plus-PR and the label gate. History is never rewritten. This record and the initial
issues were created on `main` directly, as the adoption itself is additive scaffolding, not
feature work.

**Standing obligations (also filed as tracking issues):**
- **No redistribution of Line 6 data.** The APK, extracted `assets/`, and decompiled Java
  are git-ignored and regenerated locally via `tools/extract_assets.py`. The public repo
  ships none of it. (This is interoperability / assistive-tech RE of lawfully-owned,
  discontinued hardware.)
- **Accessibility is pass/fail**, never best-effort — the whole point of the project.
- **Security hygiene:** the PAT pasted in chat during setup, and the plaintext
  `credential.helper store`, are to be rotated / migrated to a keychain helper.
