---
name: verification
description: Independently verify implemented changes against acceptance criteria, design, standards, and Definition of Done. Use for QA, code review, regression assessment, and re-verification after fixes.
---

# Verification

## Establish scope and candidate
Read the originating task, authoritative REQ/AC, baseline, relevant decisions/design, standards, and DoD. Inspect the actual diff. Identify the tested commit/build; if uncommitted changes exist, record their patch/file snapshot. A branch name alone does not pin the tested artifact. Record environment, relevant configuration, and time.

Treat developer explanations as context, not proof. Use a separate review context where possible; report limitations honestly.

## Specification review
Check required behavior, AC, business rules, permission/data-scope enforcement, alternative/failure paths, and unapproved additions. Compare to the authoritative requirements and current accepted decisions.

## Standards review
Check project conventions, accepted architecture, security/data integrity, justified complexity, contracts, and required compatibility. Keep these findings distinguishable from specification findings. Use automated tooling for mechanical rules.

## Execute and classify
Run proportionate automated, API/integration, browser, permission, and regression checks. A static review alone does not prove runtime behavior. Classify product defects, automation defects, environment failures, requirement ambiguity, and requested behavior changes.

Report each criterion Pass, Fail, or Not verified with evidence. Do not change the requirement, lower an assertion, or add arbitrary waits to force success. Return ambiguity to the orchestrator.

## Evidence and re-verification
Link results to candidate, environment, check, and time. After a fix, verify on the new candidate and rerun impacted regressions. If anything changed after the tested snapshot, tell the orchestrator that the previous Pass may be stale. Retain unaffected evidence only with a reasoned impact assessment.

## DoD and human approval
Assess each applicable DoD condition. Distinguish legitimate non-applicability from inability to execute a required check. Mandatory incomplete conditions prevent completion. Do not waive them or replace a required human code/release review with AI review.

Use Pass when required verification succeeds; Fail for demonstrated blocking defects; Blocked when required verification cannot be completed. Report both defects and verification blockers if both exist. The orchestrator determines workflow transitions.

## Return
Return task ID, outcome, candidate/environment/time, AC results/evidence, specification findings, standards findings, DoD results, reproduction details, limitations, and next action. Do not independently close tasks, merge, deploy, or change product code unless separately assigned.
