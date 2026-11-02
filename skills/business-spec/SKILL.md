---
name: business-spec
description: Create or refine Hebrew business and functional specifications from ideas, scattered source material, or existing documents. Use for overall process discovery, shared terminology, detailed requirements, and acceptance criteria for an upcoming delivery scope.
---

# Business Specification

## Source and template
Read relevant sources and existing specifications. Record source coverage and missing/unreadable material. When creating a document, read [business template](assets/business-spec.he.template.md) and copy it to the configured project path. Preserve established documents and IDs.

## Overall view first — MANDATORY SEQUENCE
Before writing any REQ-XXX identifiers:
1. **Document ALL processes** from sources at overview level (Section 4 in template): one row per process with participants, outcome, dependencies. No REQ IDs here.
2. **Present overview to stakeholder** and ask: which processes are in Phase 1 scope?
3. **Record scope decision** in decisions.md
4. **Only then** write Section 5 with detailed REQs — and only for scoped processes.

**Anti-pattern to avoid:** Reading sources → immediately writing detailed REQs for everything you see. This skips the overview step, wastes effort on unscoped items, and creates false commitments.

Establish goals, users, boundaries, major processes, shared information, external systems, and business dependencies. Group scattered material by process, consolidate duplicates, and surface contradictions. Provide enough overview to support architecture and release planning; do not require detailed fields/AC for all future scope before delivering the first capability.

## Terminology and language
Maintain a concise Hebrew–English glossary in the business specification. Resolve overloaded terms; use the same terms across requirements, tasks, code, and tests. Keep business semantics in Hebrew. This is the authoritative business source, even when English task briefs are generated. Exact Hebrew UI wording is part of the requirement when specified.

## Detail the selected scope
For each process define trigger, actors, prerequisites, outcome, normal steps, alternatives, exceptions, data/documents/screens/actions, rules/calculations/permissions, allowed state transitions, integrations/ownership, and required notifications/reports.

Assign stable REQ IDs and preserve existing ones. Link requirements to source sections and relevant decision IDs. Distinguish source facts, accepted decisions, proposals, and assumptions. Do not invent integrations, volumes, or rules.

## Screens and user journeys
For each in-scope feature, document:
- **User journeys**: Step-by-step flows from trigger to outcome (success and failure paths)
- **Screens**: Layout, navigation, actions, fields with validation rules
- **States**: Loading, empty, error, and success states for each screen
- **Permissions**: What each role can see/do on each screen

Include simple wireframes for important or novel flows. Routine screens following an already-approved pattern need only reference the pattern. For complex interactions, recommend a clickable prototype before detailed implementation.

Keep three distinctions clear:
- **Wireframe**: Layout and interaction proposal (for approval)
- **Acceptance criteria**: Observable behavior that must work (for verification)
- **Technical design**: How the screen is implemented (belongs in technical-spec)

Example: An inquiry submission screen needs more than a field list. Document what happens when:
- A required document is missing
- Submission fails (network, validation, server error)
- The user lacks permission
- Submission succeeds (confirmation, next steps)

## Acceptance criteria
Place observable AC beside each requirement or process; assign stable AC IDs for traceability. Cover success plus relevant validation/rejection, permissions/data scope, transitions, failures, and boundary cases. Use Given/When/Then when it adds clarity. Derive expected outcomes from agreed rules or examples, not inferred implementation. Record unresolved behavior as a question.

Business approval must cover user journeys and wireframes. An overall business review is different from approval of detailed scope. Before development, ensure the selected requirements and AC are clear and materially agreed.

## Quality and operations
Capture known performance, availability, accessibility, privacy, retention, and continuity needs. Use measurable targets only when agreed; mark unknown targets explicitly and identify whether they block the selected scope. Do not manufacture compliance obligations.

## Questions and updates
Propose material questions to the orchestrator with owner, impact, options, and needed-before milestone. It allocates persistent IDs and owns decisions.md. Reference those IDs in affected sections without copying the register. Incorporate routine resolved clarifications directly.

After an accepted decision, update affected requirements/AC and report changed IDs plus any remaining incorporation work. Never mark shared questions Incorporated yourself.

## Return

Return the four-field handoff report:

### 1. Changes Made
- Changed sections and REQ/AC IDs
- Sources reviewed
- Baseline referenced

### 2. Checks Performed
Before handoff, verify:
- [ ] Scope coverage: all in-scope processes have detailed requirements
- [ ] Acceptance criteria: every REQ has observable ACs
- [ ] ID stability: no IDs renumbered; new IDs use next free number
- [ ] Cross-references: all section/REQ/AC references resolve
- [ ] Terminology: terms match glossary; no term used two ways
- [ ] Section numbering: sequential, no gaps
- [ ] Rule consistency: changed rules updated in all affected places (flows, screens, permissions, exceptions, ACs)
- [ ] Spec alignment: if business spec changed, flag whether technical spec needs update
- [ ] Approval metadata: status reflects reality (draft if content changed from approved version)

### 3. Unresolved Gaps
- List gaps found that you cannot fix (need business decision, need orchestrator action)
- For each: severity BLOCKING/SIGNIFICANT/MINOR and who must resolve
- If none: "None"

### 4. Approval Impact
- Did this change content that was previously marked approved? Yes/No
- If Yes: list affected sections
- Recommendation: "No approval impact" | "Sections X,Y need re-approval" | "Document status should change from Approved to Draft"

**CRITICAL:** Never report "ready" while:
- Checks have failures
- Unresolved gaps are BLOCKING
- Approval impact shows material changes without flagging it

Do not claim approval without an actual source or write application code. Keep the document proportional; detail only current scope while maintaining the overall map.
