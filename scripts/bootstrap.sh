#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[setup] Root: $ROOT_DIR"

if [[ ! -f .env ]]; then
  cp .env.example .env
  echo "[setup] Created .env from .env.example"
else
  echo "[setup] .env already exists"
fi

echo "[setup] Installing Node dependencies"
npm install --legacy-peer-deps

PYTHON_BIN="${PYTHON_BIN:-python3}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "[setup] Python not found. Set PYTHON_BIN or install python3."
  exit 1
fi

if [[ ! -d .venv ]]; then
  echo "[setup] Creating virtual environment"
  "$PYTHON_BIN" -m venv .venv
fi

echo "[setup] Installing Python dependencies in .venv"
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.setup.txt

if command -v pg_isready >/dev/null 2>&1; then
  if pg_isready -h localhost -p 5432 >/dev/null 2>&1; then
    echo "[setup] PostgreSQL is reachable"
    if ! psql -lqt | cut -d '|' -f 1 | tr -d ' ' | grep -qx "aerospace_db"; then
      createdb aerospace_db
      echo "[setup] Created database aerospace_db"
    else
      echo "[setup] Database aerospace_db already exists"
    fi

    echo "[setup] Creating tables if missing"
    (
      cd backend
      ../.venv/bin/python -c "from app import create_app, db; app = create_app(); ctx = app.app_context(); ctx.push(); db.create_all(); ctx.pop()"
    )
  else
    echo "[setup] PostgreSQL not reachable at localhost:5432 (skipping DB init)"
  fi
else
  echo "[setup] pg_isready not found (skipping DB checks)"
fi

echo "[setup] Done. Start app with: npm run dev"
