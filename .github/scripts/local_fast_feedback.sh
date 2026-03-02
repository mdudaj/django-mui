#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

FULL_GATE=0
if [[ "${1:-}" == "--full-gate" ]]; then
  FULL_GATE=1
  shift
fi

PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
if [[ ! -x "$PYTHON_BIN" ]]; then
  python3 -m venv "$ROOT_DIR/.venv"
  "$PYTHON_BIN" -m pip install -q --upgrade pip
  "$PYTHON_BIN" -m pip install -q -r "$ROOT_DIR/requirements.txt" "ruff==0.15.4"
fi

if [[ $FULL_GATE -eq 1 ]]; then
  "$PYTHON_BIN" -m ruff check .
  "$PYTHON_BIN" -m ruff check . --select S
fi

if [[ $# -gt 0 ]]; then
  "$PYTHON_BIN" -m unittest "$@"
else
  "$PYTHON_BIN" -m unittest discover -s tests -p "test_*.py"
fi
