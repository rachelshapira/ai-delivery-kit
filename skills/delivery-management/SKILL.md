---
name: delivery-management
description: Plan delivery from specifications, coordinate readiness and completion, and manage task dependencies, questions, decisions, changes, and resumable state. Use when starting or resuming work, preparing delivery scopes or tasks, processing answers or changes, or assessing completion.
---

# Delivery Management

## Sources and templates
Use business specifications for intended behavior, technical specifications for design, the delivery record for execution, and the decision register for question/decision history.

When creating records, read [delivery template](assets/delivery.template.md) and [decision template](assets/decisions.template.md). Copy to the configured project paths; do not edit package templates as project data. Create documents when useful, not as empty mandatory paperwork.

The orchestrator owns shared delivery and decision writes. Reconcile agent reports and current file content before updating. Agents propose; they do not concurrently rewrite shared state.

## Tracker ownership
- With a tracker: tasks, dependencies, and task status live there. Keep a short local delivery checkpoint, source baselines, DoD reference, and links. No duplicate status table.
- Without a tracker: maintain task entries and status in delivery.md.
- Decisions remain in decisions.md unless an established authoritative decision system is explicitly adopted; record its location.
- Keep one authoritative DoD. Reference the organizational definition when available; otherwise agree and record it in delivery.md.

## Review and authorization boundaries
1. Overall business review confirms the system direction and major processes; it is not exhaustive approval of every future detail.
2. Agreement on delivery scopes establishes priorities, inclusions, and exclusions.
3. Before implementing a scope, confirm business behavior/AC and material technical decisions. These can be reviewed together; do not add a separate approval ritual for every document edit.
4. Merge and release approvals follow actual organizational rules.

Record real approval sources, owners, scope, and baseline. Reuse valid explicit approvals. Routine edits within that authorization do not require reapproval. New material consequences do.

## Plan delivery
Read the overall business view and initial architecture. Identify capabilities, shared prerequisites, real blocking dependencies, and risky assumptions. Propose useful end-to-end scopes with inclusions, deferred work, and dependencies. Order by agreed business priority, dependencies, and risk. Use bounded investigations when uncertainty prevents sound planning.

Do not invent business priorities, dates, or team capacity. State assumptions and ask focused questions only where they materially affect the plan. Detail the next scope rather than the whole future backlog.

## Prepare tasks
Prefer narrow, verifiable end-to-end behavior. Explicit infrastructure and investigation tasks are valid where needed. Each task has ID, outcome, REQ/AC references, baseline, relevant design/decisions, dependency IDs, change boundaries, status, work reference, and evidence.

English task briefs are derived views of the Hebrew business source. Preserve IDs and meaning. Link a source version or immutable revision. On source change, reassess affected tasks; avoid a separately maintained full translated specification.

## Readiness
Before implementation confirm clear bounded scope, observable AC, sufficient technical direction, complete required dependencies, incorporated blocking decisions, applicable scope approval, and DoD.

For investigations, define the question, allowed experiment, boundary, and expected evidence. Research/prototype results are not approved production requirements.

## Delegation contract
Send this information as a message, not another mandatory file:

```text
Task ID and objective:
Allowed scope and excluded changes:
Source baseline and REQ/AC references:
Relevant design and decision references:
Dependencies / blockers:
Work location:
Applicable DoD / standards:
Expected output:
```

Require:

```text
Task ID and outcome:
Changed artifacts / work reference:
Candidate identity:
Checks, environment, results, and evidence:
Unexecuted checks and reasons:
Remaining work:
Questions / blockers / proposed decisions:
Next action:
```

Select the smallest relevant context and skills. Sequential implementation is the default; introduce parallelism only with explicit non-conflicting boundaries and dependency control.

## States and completion
Reuse an established tracker workflow; otherwise use Pending, Ready, In progress, In verification, Blocked, Done, Cancelled. Developer handoff transitions to In verification. Failed QA returns to In progress. Preserve the previous phase and blocker on Blocked tasks.

Done requires current-candidate AC/DoD evidence, independent verification, required human review, no acceptance-blocking defects, and updated artifacts. Record release/deployment separately. Task-level checklist completion alone is insufficient to claim a release is ready: verify integration of the delivered scope.

## Definition of Done
Reuse organizational standards or propose a concise baseline for the technical owner and QA, with business input where acceptance is affected. Agree what Done means before implementation.

Cover AC, relevant builds/tests, specification and standards review, relevant permission/failure/regression checks, contracts/documentation/migrations, blocking defects, and linked evidence.

Distinguish conditional applicability from waiver:
- No schema change may make a migration condition inapplicable.
- An unavailable required integration test is Not verified, not inapplicable.
- A mandatory condition cannot be waived by the agent. A governing-DoD change needs the actual authorized owner; otherwise keep the task incomplete.

## Questions
Record only material unresolved questions, not every routine clarification. Assign stable Q-BIZ/Q-TECH IDs centrally. Include question, owner (or Unknown), impact, blocking scope, needed-before milestone, options, status, answer/source/date, affected artifacts, and pending updates.

Statuses:
- Open: no authorized answer.
- Answered: answer received, incorporation still pending.
- Incorporated: affected specifications/plans updated. This does not mean code implemented.
- Deferred: explicit revisit trigger and scope; work dependent on it remains unready.

Ask in small related batches, highest impact first, after checking existing sources. Business questions go to business owners, technical questions to technical owners. Technical investigation can supply evidence but cannot invent business authority. Continue unaffected work.

After an answer, update impacted requirements, AC, design, translated briefs, tasks, and verification scope as relevant. Track unfinished updates. Mark Incorporated only after checking them; then release affected blockers.

## Significant decisions
A question's answer normally stays in its question entry. Do not create a second DEC for the same answer. For a significant tradeoff, create DEC or ADR with context, decision, alternatives, rationale, consequences, source, and affected artifacts; let the question link to it rather than duplicate it.

Decision statuses: Proposed, Accepted, Rejected, Superseded. Preserve history and link replacements. Keep routine implementation choices out of the ADR register. Technical documents describe the current design and reference ADR history.

## Changes and evidence freshness
Classify draft clarification, defect against agreed behavior, or requirement/design change. Assess affected REQ/AC, design, code/data, tasks/dependencies, verification, and delivery order. Reuse existing authorization; ask only for unresolved material consequences. Update specifications and pending tasks; create linked change tasks for completed work. Preserve history and pause only affected work.

Evidence must identify the tested candidate, environment, time, and check/result. A branch name alone is not enough: prefer commit/build identity. If uncommitted changes were tested, capture a patch or file-hash snapshot and disclose it.

After code, dependency, configuration, or relevant requirement changes, assess stale evidence. Rerun affected checks on the new candidate; retain other evidence only with a stated rationale. Never carry Pass forward blindly.

## Checkpoint and partial-update recovery
Keep phase, scope, source baselines, active task/work reference, completed/remaining work, blockers/question IDs, unfinished artifact updates, and one concrete next action. Update after meaningful transitions and before stopping.

On resume reconcile against actual artifacts. For a decision interrupted during incorporation, inspect completed updates, finish missing ones, and only then mark Incorporated. Never interpret a partially updated specification as an implemented or fully approved change. Use existing version control to preserve history; no custom transaction engine is required.

## Failure and delivery
Distinguish product failure from missing access/environment. Stop repeated unchanged failing attempts without new evidence; summarize attempts and propose the next diagnostic action. Never report unavailable checks as passed.

For deployment-affecting changes, include relevant migration, monitoring, and recovery steps in existing task/design records. Present the result and remaining limitations. After a delivered scope, capture concrete friction and adjust only the instruction or check it justifies.
