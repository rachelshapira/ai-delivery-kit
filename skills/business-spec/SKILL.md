---
name: business-spec
description: Create or refine Hebrew business and functional specifications from ideas, scattered source material, or existing documents. Use for overall process discovery, shared terminology, detailed requirements, and acceptance criteria for an upcoming delivery scope.
---

# Business Specification

## Source and template
Read relevant sources and existing specifications. Record source coverage and missing/unreadable material. When creating a document, read [business template](assets/business-spec.he.template.md) and copy it to the configured project path. Preserve established documents and IDs.

## Overall view first
Establish goals, users, boundaries, major processes, shared information, external systems, and business dependencies. Group scattered material by process, consolidate duplicates, and surface contradictions. Provide enough overview to support architecture and release planning; do not require detailed fields/AC for all future scope before delivering the first capability.

## Terminology and language
Maintain a concise Hebrew–English glossary in the business specification. Resolve overloaded terms; use the same terms across requirements, tasks, code, and tests. Keep business semantics in Hebrew. This is the authoritative business source, even when English task briefs are generated. Exact Hebrew UI wording is part of the requirement when specified.

## Detail the selected scope
For each process define trigger, actors, prerequisites, outcome, normal steps, alternatives, exceptions, data/documents/screens/actions, rules/calculations/permissions, allowed state transitions, integrations/ownership, and required notifications/reports.

Assign stable REQ IDs and preserve existing ones. Link requirements to source sections and relevant decision IDs. Distinguish source facts, accepted decisions, proposals, and assumptions. Do not invent integrations, volumes, or rules.

## Acceptance criteria
Place observable AC beside each requirement or process; assign stable AC IDs for traceability. Cover success plus relevant validation/rejection, permissions/data scope, transitions, failures, and boundary cases. Use Given/When/Then when it adds clarity. Derive expected outcomes from agreed rules or examples, not inferred implementation. Record unresolved behavior as a question.

An overall business review is different from approval of detailed scope. Before development, ensure the selected requirements and AC are clear and materially agreed.

## Quality and operations
Capture known performance, availability, accessibility, privacy, retention, and continuity needs. Use measurable targets only when agreed; mark unknown targets explicitly and identify whether they block the selected scope. Do not manufacture compliance obligations.

## Questions and updates
Propose material questions to the orchestrator with owner, impact, options, and needed-before milestone. It allocates persistent IDs and owns decisions.md. Reference those IDs in affected sections without copying the register. Incorporate routine resolved clarifications directly.

After an accepted decision, update affected requirements/AC and report changed IDs plus any remaining incorporation work. Never mark shared questions Incorporated yourself.

## Return
Return changed sections, REQ/AC IDs, sources reviewed, baseline, open questions, dependencies, and readiness. Do not claim approval without an actual source or write application code. Keep the document proportional; detail only current scope while maintaining the overall map.
