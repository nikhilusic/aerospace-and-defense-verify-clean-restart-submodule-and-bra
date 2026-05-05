# aerospace-and-defense-verify-clean-restart-submodule-and-bra Constitution

Generated on 2026-05-05 through the technology selection workflow.
Regenerated at: 2026-05-05T14:41:36.561Z
Trigger source: ui-push-story

This constitution defines the baseline engineering standards for the project and applies Siemens-inspired software design principles as mandatory delivery guidance.

## Technology Baseline

- Industry domain: Consumer Package Goods
- Architecture pattern: Microservices
- Frontend stack: Angular
- Backend stack: Python
- Database stack: PostgreSQL
- Deployment environment: AWS

## Siemens Standard Design Pattern Alignment

The selected architecture (Microservices) is implemented using Siemens-style engineering expectations: explicit system boundaries, clear interface contracts, traceability, reliability, and maintainable modular decomposition.

### Architecture-Specific Implementation Guidance

1. Define service boundaries by business capability and avoid cross-service schema leakage.
2. Require explicit API contracts, observability, and fault isolation across service calls.
3. Adopt eventual consistency patterns where synchronous coupling would reduce resilience.

## Core Principles

### 1. Architecture Integrity
All implementation work MUST preserve the Microservices architectural boundaries and keep responsibilities explicit across UI, service, and persistence layers.

### 2. Stack-Driven Consistency
Frontend work MUST align with Angular, backend work MUST align with Python, data access MUST align with PostgreSQL, and runtime delivery MUST align with AWS. Divergence requires an explicit justification in the implementation plan.

### 3. Design Guideline Enforcement
User-facing behavior MUST follow the selected design direction and remain accessible, responsive, and understandable under success, loading, and failure states.

### 4. Verification First
Every feature increment MUST define acceptance criteria coverage, integration touchpoints, and at least one automated verification path for business-critical behavior.

### 5. Operational Readiness
Generated code MUST include observable failure modes, safe defaults, clear state transitions, and maintainable naming so future iterations stay auditable.

## Stack-Specific Guardrails

1. Frontend guardrail (Angular): preserve reusable component composition, deterministic state transitions, and accessibility-focused UI behavior.
2. Backend guardrail (Python): expose stable API contracts, validate all external input, and keep domain logic outside transport adapters.
3. Database guardrail (PostgreSQL): define schema or document contracts early, codify migrations, and protect data integrity and consistency.
4. Deployment guardrail (AWS): enforce environment parity, security hardening, deployment rollback strategy, and operational monitoring baselines.

## Delivery Quality Gates

1. Requirement Traceability: every implementation PR maps to a user story and acceptance criteria.
2. Architecture Conformance: code changes respect chosen pattern boundaries and review checklist.
3. Test Coverage: include happy path, failure path, and one edge scenario for critical flows.
4. Operational Readiness: log meaningful events and expose diagnostics for triage.
5. Security and Compliance: validate permissions, sanitize input, and avoid sensitive data leakage.

## Mandatory Engineering Guidelines

1. Use secure-by-default input validation, output encoding, and dependency hygiene.
2. Preserve accessibility, responsive behavior, and user feedback for every workflow state.
3. Keep components cohesive, APIs explicit, and data contracts testable.
4. Prefer observability, meaningful logging, and failure handling over silent fallback behavior.
5. Add automated verification for critical user paths, business rules, and integration boundaries.
6. Apply a System, Component, and Interface decomposition with explicit ownership boundaries.
7. Keep contracts versioned and backward-compatible where possible; document breaking changes explicitly.
8. Design for reliability: graceful degradation, deterministic error handling, and measurable recovery paths.
9. Enforce traceability from requirement to story, acceptance criteria, tests, and implementation artifacts.
10. Use security and privacy by design: least privilege, validated inputs, and auditable operational events.
11. Protect maintainability with modular code, clear naming, and architecture conformance checks in reviews.
