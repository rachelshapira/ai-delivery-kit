---
name: implementation
description: Implement a defined feature, change, or defect fix in small verifiable increments using project standards and relevant technology skills. Use after scope and acceptance criteria are sufficiently clear.
---

# Implementation

## Prepare
Read the assignment contract, authoritative REQ/AC, technical design, decisions, standards, and DoD. Check the source baseline before trusting an English task brief. Inspect actual code and reusable capabilities. Report blocking inconsistency; do not silently reconcile conflicting business behavior.

## Build
Implement one coherent behavior at a time across the necessary data, backend, and UI. Follow established patterns, use relevant technology skills, and preserve unrelated changes. Avoid speculative features and unrelated refactoring. Respect allowed scope and tool permissions.

## Feedback during development
Choose checks proportional to behavior and risk. For business rules, calculations, and reproducible bugs, prefer a failing test expressing the agreed outcome, then the smallest correct change and relevant regression checks. For other work use appropriate integration, browser, static-analysis, or build feedback.

Test observable behavior through suitable interfaces. Derive expected values from AC or independently worked examples. Do not reproduce implementation logic in assertions. Use test doubles only where suitable; verify real integration behavior when required. Never weaken assertions merely to pass.

## Questions and changes
Report missing behavior, source/code contradictions, contract/architecture changes, and dependency/environment blockers. Continue unaffected work. The orchestrator owns shared status and decisions. Do not mutate requirements or DoD to justify a shortcut.

## Candidate and evidence
Record what was tested: commit/build if available, plus relevant configuration/environment and commands/results. If the working tree is dirty, disclose it and identify the tested patch or file snapshot. Do not label a test run as evidence for a clean commit when it included other changes.

After additional code, dependency, configuration, or relevant requirement changes, reassess affected checks. Report changes made after QA handoff explicitly. Keep evidence references durable enough for review and resume; avoid secrets in reports.

## Return
Use the assignment return contract: outcome, artifacts/work reference, candidate identity, REQ/AC addressed, executed checks/results/evidence, unexecuted checks/reasons, remaining work, blockers, and next action. Include startup/reproduction and applicable migration/recovery instructions.

Report Ready for verification, not Done. Do not claim independent QA or bypass merge/deployment controls. If repeated attempts fail without new information, stop and report diagnosis needs.
