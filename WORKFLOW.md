# Project Workflow

## The Flow

```
SCOPE ──▶ SPEC ──▶ DESIGN ──▶ TASKS ──▶ BUILD ──▶ DONE
   │         │         │          │         │        │
validate  validate  validate  validate   review   verify
   │         │         │          │         │        │
   ✓         ✓         ✓          ✓         ✓        ✓
  Biz       Biz      Tech       Team      Code      QA
```

## Six Stages

| # | Stage | Do | Validate | Approve | Output |
|---|-------|-----|----------|---------|--------|
| 1 | SCOPE | List processes, decide in/out | All listed? Decision clear? | Business | decisions.md |
| 2 | SPEC | Write REQs + ACs | REQ per feature? AC testable? | Business | business-spec.he.md |
| 3 | DESIGN | Write APIs, data model | API per REQ? Test per AC? | Tech Lead | technical-spec.md |
| 4 | TASKS | Break into work items | Task per REQ? Estimated? | Team | delivery.md |
| 5 | BUILD | Write code | Code review pass? | Reviewer | PR merged |
| 6 | DONE | Test | All ACs pass? | QA | Verified |

## Files

```
decisions.md          ← scope + big decisions
business-spec.he.md   ← requirements (Hebrew)
technical-spec.md     ← architecture + APIs
delivery.md           ← tasks + status
```

## Rules

1. **Validate before approve** — no approval without passing checks
2. **No skipping stages** — each stage builds on the previous
3. **Changes go back** — if spec changes, re-validate from that stage
