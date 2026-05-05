#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

DB_NAME="${DB_NAME:-aerospace_db}"

echo "[db] Using database: $DB_NAME"

if ! command -v pg_isready >/dev/null 2>&1; then
  echo "[db] pg_isready not found. Install PostgreSQL client tools first."
  exit 1
fi

if ! pg_isready -h localhost -p 5432 >/dev/null 2>&1; then
  echo "[db] PostgreSQL is not reachable at localhost:5432"
  exit 1
fi

if ! psql -lqt | cut -d '|' -f 1 | tr -d ' ' | grep -qx "$DB_NAME"; then
  createdb "$DB_NAME"
  echo "[db] Created database $DB_NAME"
fi

PAGER=cat psql -d "$DB_NAME" <<'SQL'
BEGIN;

CREATE TABLE IF NOT EXISTS requirements (
  id UUID PRIMARY KEY,
  creation_date TIMESTAMP NOT NULL DEFAULT NOW(),
  modification_date TIMESTAMP NOT NULL DEFAULT NOW(),
  creator VARCHAR(255),
  producer VARCHAR(255),
  title VARCHAR(512) NOT NULL,
  description TEXT,
  status VARCHAR(50) NOT NULL DEFAULT 'draft',
  priority VARCHAR(50),
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS user_stories (
  id UUID PRIMARY KEY,
  requirement_id UUID NOT NULL REFERENCES requirements(id),
  title VARCHAR(512) NOT NULL,
  description TEXT,
  acceptance_criteria TEXT,
  status VARCHAR(50) NOT NULL DEFAULT 'draft',
  priority VARCHAR(50),
  estimated_effort INTEGER,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

TRUNCATE TABLE user_stories, requirements;

INSERT INTO requirements (
  id, creation_date, modification_date, creator, producer, title, description, status, priority, created_at, updated_at
) VALUES
  ('dcc82398-e3ad-450c-a44c-6d5dabe104b8'::uuid, NOW(), NOW(), 'Program Lead', 'Flight Ops', 'Flight readiness certification package', 'Coordinate readiness evidence and certification sign-off for monthly gate.', 'approved', 'high', NOW(), NOW()),
  ('8b2f2f20-b4fd-4ba3-9d9d-101be5591111'::uuid, NOW(), NOW(), 'Program Office', 'Systems Integration', 'Avionics regression closure plan', 'Track unresolved avionics test regressions before release candidate cut.', 'approved', 'high', NOW(), NOW()),
  ('8b2f2f20-b4fd-4ba3-9d9d-101be5592222'::uuid, NOW(), NOW(), 'QA Lead', 'Propulsion Team', 'Engine control software verification pack', 'Assemble evidence set for FADEC verification and audit readiness.', 'in_progress', 'high', NOW(), NOW()),
  ('8b2f2f20-b4fd-4ba3-9d9d-101be5593333'::uuid, NOW(), NOW(), 'Chief Engineer', 'Structures Group', 'Airframe structural fatigue review', 'Consolidate NDI findings and close fatigue-related engineering actions.', 'draft', 'medium', NOW(), NOW()),
  ('8b2f2f20-b4fd-4ba3-9d9d-101be5594444'::uuid, NOW(), NOW(), 'Ops Director', 'Safety Office', 'Ground operations safety drill readiness', 'Ensure emergency response drills are scheduled and certified across teams.', 'approved', 'medium', NOW(), NOW()),
  ('8b2f2f20-b4fd-4ba3-9d9d-101be5595555'::uuid, NOW(), NOW(), 'Compliance Lead', 'Supply Chain QA', 'Supplier qualification traceability uplift', 'Align supplier qualification artifacts with certification trace matrix.', 'in_progress', 'high', NOW(), NOW());

INSERT INTO user_stories (
  id, requirement_id, title, description, acceptance_criteria, status, priority, estimated_effort, created_at, updated_at
) VALUES
  ('140335b6-ab81-4885-81af-364a79864fdc'::uuid, 'dcc82398-e3ad-450c-a44c-6d5dabe104b8'::uuid, 'Review missing verification artifacts', 'Identify missing evidence before monthly certification review.', 'All required artifacts attached and traceable.', 'in_progress', 'high', 8, NOW(), NOW()),
  ('458861a3-59d0-4a15-bd1f-0d06e8928678'::uuid, 'dcc82398-e3ad-450c-a44c-6d5dabe104b8'::uuid, 'Escalate critical safety hazard backlog', 'Surface overdue hazards to program leadership.', 'Critical backlog visible in command center with owner assigned.', 'draft', 'high', 5, NOW(), NOW()),
  ('bf47a7d0-65a1-41bb-bec1-201be5591111'::uuid, '8b2f2f20-b4fd-4ba3-9d9d-101be5591111'::uuid, 'Triage open autopilot regression defects', 'Categorize open autopilot defects by severity and owner.', 'All open defects have severity, owner, and ETA recorded.', 'in_progress', 'high', 8, NOW(), NOW()),
  ('bf47a7d0-65a1-41bb-bec1-201be5592222'::uuid, '8b2f2f20-b4fd-4ba3-9d9d-101be5591111'::uuid, 'Publish weekly avionics burn-down', 'Automate weekly defect burn-down and share with leadership.', 'Dashboard is updated weekly and reviewed in standup.', 'draft', 'medium', 5, NOW(), NOW()),
  ('bf47a7d0-65a1-41bb-bec1-201be5593333'::uuid, '8b2f2f20-b4fd-4ba3-9d9d-101be5592222'::uuid, 'Collect FADEC integration logs', 'Gather integration logs from bench and flight simulation runs.', 'All required run logs are attached and signed.', 'in_progress', 'high', 8, NOW(), NOW()),
  ('bf47a7d0-65a1-41bb-bec1-201be5594444'::uuid, '8b2f2f20-b4fd-4ba3-9d9d-101be5592222'::uuid, 'Map verification evidence to requirements', 'Link each test artifact to certification requirements.', 'Every requirement has at least one linked evidence artifact.', 'draft', 'high', 6, NOW(), NOW()),
  ('bf47a7d0-65a1-41bb-bec1-201be5595555'::uuid, '8b2f2f20-b4fd-4ba3-9d9d-101be5593333'::uuid, 'Prioritize fatigue hotspots for rework', 'Rank hotspots by risk and rework effort.', 'Top 10 hotspots approved by structures lead.', 'draft', 'medium', 5, NOW(), NOW()),
  ('bf47a7d0-65a1-41bb-bec1-201be5596666'::uuid, '8b2f2f20-b4fd-4ba3-9d9d-101be5594444'::uuid, 'Assign drill captains by site', 'Name accountable captains for each operating location.', 'Each site has a captain and backup assigned.', 'done', 'medium', 3, NOW(), NOW()),
  ('bf47a7d0-65a1-41bb-bec1-201be5597777'::uuid, '8b2f2f20-b4fd-4ba3-9d9d-101be5594444'::uuid, 'Validate emergency equipment checklist', 'Audit emergency kits and reporting channels.', 'Checklist is completed for all active sites.', 'in_progress', 'medium', 4, NOW(), NOW()),
  ('bf47a7d0-65a1-41bb-bec1-201be5598888'::uuid, '8b2f2f20-b4fd-4ba3-9d9d-101be5595555'::uuid, 'Backfill missing supplier test certificates', 'Request and upload missing supplier test certs.', 'All tier-1 suppliers have current certificates attached.', 'in_progress', 'high', 7, NOW(), NOW()),
  ('bf47a7d0-65a1-41bb-bec1-201be5599999'::uuid, '8b2f2f20-b4fd-4ba3-9d9d-101be5595555'::uuid, 'Standardize supplier audit scorecards', 'Normalize scoring rubric across supply chain audits.', 'Scorecards use common rubric and are approved by compliance.', 'draft', 'medium', 5, NOW(), NOW());

COMMIT;

SELECT COUNT(*) AS requirements_count FROM requirements;
SELECT COUNT(*) AS user_stories_count FROM user_stories;
SQL

echo "[db] Reset + seed complete"
