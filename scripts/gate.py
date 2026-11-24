"""FreedomHawk local gate — must pass before any PR opens.

Run with the project venv's Python:  .venv\\Scripts\\python scripts\\gate.py

Checks, in order: the package byte-compiles, ruff (only if installed — it is optional here),
then the full test suite. Exits non-zero on the first failure. Grow this when a defect class
recurs (per the playbook); keep it honest — a green gate must mean something.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable


def step(name: str, cmd: list[str], *, optional: bool = False) -> bool:
    print(f"\n=== {name} ===", flush=True)
    try:
        rc = subprocess.run(cmd, cwd=ROOT).returncode
    except FileNotFoundError:
        if optional:
            print(f"(skipped — {cmd[0]} not installed)")
            return True
        print(f"FAIL: {cmd[0]} not found")
        return False
    if rc != 0 and optional:
        print(f"(non-blocking: {name} returned {rc})")
        return True
    return rc == 0


def main() -> int:
    ok = True
    ok &= step("compile", [PY, "-m", "compileall", "-q", "src"])
    ok &= step("ruff (optional)", [PY, "-m", "ruff", "check", "src", "tests"], optional=True)
    ok &= step("tests", [PY, "-m", "pytest", "-q"])
    print("\n" + ("GATE PASSED" if ok else "GATE FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
