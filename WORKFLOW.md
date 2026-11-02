# Project Workflow

## The Flow

```
SCOPE → SPEC → DESIGN → TASKS → BUILD → DONE
  ↓       ↓       ↓        ↓       ↓       ↓
 Biz     Biz    Tech     Team    Code    QA
 ✓       ✓       ✓        ✓       ✓       ✓
```

## Six Stages

| # | Stage | Output | Approver | Done When |
|---|-------|--------|----------|-----------|
| 1 | **SCOPE** | What's in/out | Business | decisions.md updated |
| 2 | **SPEC** | Requirements | Business | business-spec.he.md approved |
| 3 | **DESIGN** | How to build | Tech Lead | technical-spec.md approved |
| 4 | **TASKS** | Work breakdown | Team | delivery.md has tasks |
| 5 | **BUILD** | Code | Reviewer | PR merged |
| 6 | **DONE** | Working software | QA | ACs verified |

## Before Each Approval

Quick check — answer YES to all:

| Stage | Check |
|-------|-------|
| SCOPE | All processes listed? In/out decided? |
| SPEC | Every feature has REQ? Every REQ has testable AC? |
| DESIGN | Every REQ has API? Every AC has test? |
| TASKS | Every REQ has task? Estimates done? |

## Files

```
decisions.md          ← scope + big decisions
business-spec.he.md   ← requirements (Hebrew)
technical-spec.md     ← architecture + APIs
delivery.md           ← tasks + status
```

## Rules

1. **No skipping stages**
2. **No next stage without approval**
3. **Changes go back to the right stage**
