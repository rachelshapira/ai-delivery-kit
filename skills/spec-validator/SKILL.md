---
name: spec-validator
description: Validates specs are complete and aligned before approval. Run at each stage gate.
---

# Spec Validator

## Purpose

Check for gaps between documents before approval. Simple checklist — pass or fail.

## When to Run

```
After DISCOVER  → validate scope is clear
After SPECIFY   → validate business spec complete
After DESIGN    → validate technical spec aligned
After PLAN      → validate tasks cover all REQs
```

## Validation Checklists

### 1. Scope Validation (before business spec)

```
□ All processes from sources listed in overview (§4)
□ In-scope / out-of-scope decision recorded in decisions.md
□ No open blocking questions (Q-XXX with status: blocking)
```

**Output:** PASS or list of gaps

---

### 2. Business Spec Validation (before technical spec)

```
□ Every in-scope process has REQ-XXX entries
□ Every REQ has at least one AC-XXX-YY
□ Every AC is testable (has expected outcome)
□ Glossary covers all domain terms
□ Users and permissions defined
□ Non-functional requirements listed
□ Sources referenced
□ Status = "בסקירה" or "מאושר"
```

**Output:** PASS or list of gaps

---

### 3. Technical Spec Validation (before tasks)

```
□ Every REQ has matching API endpoint(s)
□ Every entity needed by APIs exists in data model
□ Every AC has verification approach in §9
□ Auth covers all user roles from business spec
□ All ADRs from decisions.md are incorporated
□ No TODO/TBD markers left
□ Status = "In Review" or "Approved"
```

**Output:** PASS or list of gaps

---

### 4. Task Validation (before implementation)

```
□ Every REQ is covered by at least one task
□ Tasks have estimates
□ Dependencies are defined
□ No circular dependencies
□ Definition of Done is complete
```

**Output:** PASS or list of gaps

---

## Gap Report Format

```markdown
## Spec Validation Report

**Stage:** [Business Spec / Technical Spec / Tasks]
**Date:** YYYY-MM-DD
**Result:** PASS / FAIL (N gaps)

### Gaps Found

| # | Type | Location | Issue | Fix |
|---|------|----------|-------|-----|
| 1 | Missing AC | REQ-005 | No acceptance criteria | Add AC-005-XX |
| 2 | No API | REQ-009 | Certificate endpoint missing | Add to §4 |
| 3 | No test | AC-007-03 | No verification approach | Add to §9 |

### Recommendation

[ ] Fix gaps before approval
[ ] Approve with gaps as known issues (add to delivery.md)
```

## Integration with Approval Flow

```
DRAFT → VALIDATE → FIX GAPS → VALIDATE → CHECKPOINT → APPROVE
              ↑         │
              └─────────┘
              (loop until PASS)
```
