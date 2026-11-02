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

## Mandatory Completeness Sections — REQUIRED BEFORE APPROVAL

The spec MUST include these sections with actual content (not placeholders). If information is unavailable, record it as an open question — do not leave gaps unaddressed.

### Permissions Matrix (Section 2.1)
Create an explicit matrix showing:
- **Rows:** Every action in the system (view, create, edit, delete, approve, etc.)
- **Columns:** Every role (provider, staff, admin, etc.)
- **Cells:** ✓ allowed, ✗ denied, or condition (e.g., "own data only")

**Anti-pattern:** Scattered permission mentions in REQs without consolidated view. If REQ-001 says "providers can upload" and REQ-006 says "staff can approve," the matrix must show BOTH and make clear what providers CANNOT do and what staff CANNOT do.

### Exception & Error Handling (Per Process)
For each PROC-XXX, explicitly document:
1. **Validation failures**: What happens when input is invalid? (field-level vs form-level errors, Hebrew error messages)
2. **Authorization failures**: What happens when user lacks permission? (redirect? error message? hide action?)
3. **System failures**: Network errors, server errors, timeouts — what does user see?
4. **Business rule violations**: What happens when action violates a rule? (e.g., upload during freeze period)
5. **Recovery paths**: Can user retry? Fix and resubmit? Contact support?

**Anti-pattern:** Only documenting the happy path. If the spec only says "user uploads document" without saying what happens when upload fails, the spec is incomplete.

### Role Definitions (Section 2)
Every role mentioned MUST have:
- **Definition**: Who is this role? (external provider user, internal nursing dept staff, system admin)
- **Goal**: What do they want to accomplish?
- **Actions**: Complete list of what they can do (cross-reference to permissions matrix)
- **Data scope**: What data can they see? (own provider only? all providers? filtered by region?)

**Anti-pattern:** Inventing roles in mid-document without defining them. If AC-006-02 says "staff can change status" but Section 2 doesn't define "staff," the spec is incomplete.

### Business Rules Catalog (Section 5.X)
Create an explicit numbered list of business rules:
- **BR-001**: File size limit: 10MB maximum per document
- **BR-002**: Allowed file types: PDF, JPG, PNG only
- **BR-003**: Rejection requires reason: Cannot reject without explanation

Rules must be explicit, not inferred. If the spec says "valid documents" without defining valid, record "define document validity criteria" as an open question.

### Screen-to-AC Traceability (Per Screen)
For each screen documented:
- **Every action** (button, link, form submit) must trace to an AC
- **Every state** (loading, empty, error, success) must be specified
- **Every field** must show: required/optional, validation rules, error message

**Anti-pattern:** Describing a screen with "upload button" without saying what AC covers the upload, what happens on success, what happens on failure, and what the button is disabled when.

## Completeness Checklist — RUN BEFORE HANDOFF

Before returning the handoff report, verify ALL of these:

### Permissions
- [ ] Permissions matrix exists in Section 2.1
- [ ] Every role in Section 2 appears in matrix columns
- [ ] Every action in REQs appears in matrix rows
- [ ] No permission mentioned in REQ without matrix entry
- [ ] Negative permissions explicit (what roles CANNOT do)

### Exception Handling
- [ ] Every PROC-XXX has exception handling section
- [ ] Validation failure behavior documented
- [ ] Authorization failure behavior documented  
- [ ] System error behavior documented
- [ ] Hebrew error messages specified (or marked as open question)

### Role Coverage
- [ ] Every role mentioned anywhere is defined in Section 2
- [ ] Every role has goal, actions, data scope
- [ ] No orphan role references (role mentioned but undefined)

### Business Rules
- [ ] Business rules cataloged with BR-XXX IDs
- [ ] Rules are explicit, not "valid," "appropriate," "correct"
- [ ] Each rule has enforcement point (which REQ/AC enforces it)

### Screen Completeness
- [ ] Every screen has all states documented (loading, empty, error, success)
- [ ] Every action traces to an AC
- [ ] Every field has validation rules
- [ ] Error messages specified in Hebrew

### Process Structure
- [ ] Every PROC-XXX has: trigger, actors, happy path, exception path, outcome
- [ ] No PROC mentioned without full structure
- [ ] Process dependencies documented (which PROC depends on which)

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

**Document Hygiene:**
- [ ] Scope coverage: all in-scope processes have detailed requirements
- [ ] Acceptance criteria: every REQ has observable ACs
- [ ] ID stability: no IDs renumbered; new IDs use next free number
- [ ] Cross-references: all section/REQ/AC references resolve
- [ ] Terminology: terms match glossary; no term used two ways
- [ ] Section numbering: sequential, no gaps
- [ ] Rule consistency: changed rules updated in all affected places (flows, screens, permissions, exceptions, ACs)
- [ ] Spec alignment: if business spec changed, flag whether technical spec needs update
- [ ] Approval metadata: status reflects reality (draft if content changed from approved version)

**Business Completeness (BLOCKING if any fail):**
- [ ] Permissions matrix: exists, covers all roles × all actions
- [ ] Exception handling: every PROC has validation/auth/system error handling
- [ ] Role coverage: every role defined with goal, actions, data scope
- [ ] Business rules: cataloged with BR-XXX IDs, explicit (not vague)
- [ ] Screen states: loading, empty, error, success documented
- [ ] Action traceability: every screen action traces to an AC
- [ ] Error messages: Hebrew messages specified or marked as question

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
