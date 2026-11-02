---
name: change-management
description: Standard workflows for updating specifications, decisions, and technology choices. Use when requirements change, technology decisions are made, or scope adjustments are needed.
---

# Change Management

## Document Ownership

| Document | Contains | Language | Owner |
|----------|----------|----------|-------|
| `business-spec.he.md` | What the system does — requirements, rules, AC | Hebrew | Business/Product |
| `technical-spec.md` | How to build it — architecture, APIs, data model | English | Technical Lead |
| `decisions.md` | Why we decided — questions, answers, ADRs | English | All (orchestrator writes) |
| `delivery.md` | Where we are — phase, tasks, status | English | Project Lead |

---

## Workflow 1: Business Requirement Change

**Trigger:** New feature, changed rule, modified acceptance criteria

```
1. UPDATE business-spec.he.md
   - Add/modify REQ-XXX with clear behavior
   - Add/modify AC-XXX-YY with testable criteria
   - Link to source if applicable

2. UPDATE technical-spec.md
   - §4 API Contracts: add/modify endpoints
   - §3 Data Design: add/modify entities/fields
   - §9 Verification Mapping: add test approach

3. UPDATE delivery.md (if scope changes)
   - Update scope tables
   - Update Definition of Done if needed

4. VERIFY sync
   - Every REQ has matching API design
   - Every AC has verification approach
```

**Example:** Add document expiry tracking
- business-spec.he.md: Add to REQ-002 "לכל מסמך תאריך תוקף"
- technical-spec.md: Add `ExpiryDate` to Document entity, add to API response
- No delivery.md change (same scope)

---

## Workflow 2: Technology Change

**Trigger:** Different database, framework, library, or infrastructure choice

```
1. ADD ADR to decisions.md
   ### ADR-XXX: [Title]
   - Status: Proposed → Accepted/Rejected
   - Date: YYYY-MM-DD
   - Context: Why considering this change
   - Options: What alternatives exist
   - Decision: What we chose
   - Consequences: What changes as a result

2. UPDATE technical-spec.md (if accepted)
   - §1 Constraints and Architecture: update stack
   - §3 Data Design: if data model affected
   - §4 API Contracts: if API patterns affected
   - §7 Client: if frontend affected
   - §8 Runtime: if deployment affected

3. UPDATE delivery.md
   - Note any task/timeline impact

4. NO CHANGE to business-spec.he.md
   - Technology is invisible to business requirements
```

**Example:** Switch from PostgreSQL to MongoDB
- decisions.md: Add ADR-004 with context and consequences
- technical-spec.md: Update §1 stack, rewrite §3 data design
- delivery.md: Note migration task needed

---

## Workflow 3: Question Answered

**Trigger:** Open question (Q-XXX) gets an answer

```
1. UPDATE decisions.md
   - Change Status: Open → Answered
   - Add Answer with date
   - Set Incorporated: Pending

2. UPDATE affected spec
   - If business question → business-spec.he.md
   - If technical question → technical-spec.md
   - Apply the decision to the design

3. UPDATE decisions.md again
   - Set Incorporated: Yes — [document] [section]

4. UPDATE delivery.md
   - Remove from blockers if it was blocking
```

**Example:** Q-TECH-001 (Legacy integration) answered
- decisions.md: Answer = "REST API with daily sync"
- technical-spec.md: Update §5 Integrations with API contract
- decisions.md: Mark incorporated

---

## Workflow 4: Scope Change

**Trigger:** Add/remove processes or features from current phase

```
1. UPDATE decisions.md
   - Add scope decision with rationale
   - Document what's in/out and why

2. UPDATE business-spec.he.md
   - §5 Scope: update in/out tables
   - §6 Detail: add REQs if scope expanded, or note "deferred" if reduced

3. UPDATE technical-spec.md
   - Add/remove APIs, entities, screens
   - Update §9 verification mapping

4. UPDATE delivery.md
   - Update scope tables
   - Update Definition of Done
   - Update task list
```

**Example:** Add PROC-05 (Communication Log) to Phase 1
- decisions.md: "DEC-002: Include PROC-05 in Phase 1 because..."
- business-spec.he.md: Add REQ-012, REQ-013 with ACs
- technical-spec.md: Add CommunicationLog entity, APIs, screens
- delivery.md: Update scope, add tasks

---

## Workflow 5: Bug or Gap Found During Implementation

**Trigger:** Spec doesn't match reality, missing case discovered

```
1. DETERMINE type:
   - Missing business rule → Workflow 1
   - Technical constraint → Workflow 2
   - Ambiguity needing decision → Workflow 3
   - Scope issue → Workflow 4

2. ASK if unclear
   - Add Q-XXX to decisions.md
   - Mark as blocker in delivery.md if blocking

3. UPDATE specs once resolved
   - Follow appropriate workflow above

4. NEVER change code without updating spec
   - Spec is source of truth
   - Code implements spec
```

---

## Quick Reference Table

| I want to... | Update | Add ADR? |
|--------------|--------|----------|
| Add a feature | business-spec → technical-spec | No |
| Change a business rule | business-spec → technical-spec | No |
| Change database | decisions → technical-spec | Yes |
| Change framework | decisions → technical-spec | Yes |
| Add a library | technical-spec only | No (unless major) |
| Change API structure | technical-spec only | No (unless breaking) |
| Answer open question | decisions → affected spec | No |
| Change Phase 1 scope | decisions → both specs → delivery | Yes |
| Fix spec ambiguity | affected spec only | No |

---

## Anti-Patterns to Avoid

1. **Code without spec** — Never implement something not in the spec. Update spec first.

2. **Tech in business spec** — Business spec describes *what*, not *how*. No API details, no database names.

3. **Business rules in tech spec** — Don't invent rules in technical spec. All rules come from business spec.

4. **Orphan decisions** — Every ADR must be incorporated into a spec. "Decided but not documented" = not decided.

5. **Scope creep without decision** — Adding features without updating decisions.md and delivery.md.

6. **Specs out of sync** — If business spec has REQ-015 but technical spec doesn't, something is wrong.

---

## Checklist Before Implementation

- [ ] All REQs in business-spec have matching APIs in technical-spec
- [ ] All ACs have verification approach in technical-spec §9
- [ ] All open questions (Q-XXX) are either answered or not blocking
- [ ] All ADRs are incorporated into technical-spec
- [ ] delivery.md reflects current scope and phase
- [ ] Definition of Done is complete and testable
