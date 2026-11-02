# Project Workflow

## The Flow

```
SCOPE ──▶ SPEC ──▶ DESIGN ──▶ TASKS ──▶ BUILD ──▶ DONE
```

## Six Stages

| # | Stage | Do | Skill | Validate | Approve | Output |
|---|-------|-----|-------|----------|---------|--------|
| 1 | SCOPE | Decide what's in/out | grilling | All processes listed? | Business | decisions.md |
| 2 | SPEC | Write requirements | business-spec | REQ per feature? AC testable? | Business | business-spec.he.md |
| 3 | DESIGN | Write architecture | technical-spec | API per REQ? Test per AC? | Tech Lead | technical-spec.md |
| 4 | TASKS | Break into tickets | to-tickets | Task per REQ? Estimated? | Team | delivery.md |
| 5 | BUILD | Write code | ponytail + tdd | Code review pass? | Reviewer | PR merged |
| 6 | DONE | Verify | code-review | All ACs pass? | QA | Verified |

## Skills by Stage

```
SCOPE   → grilling (stress-test decisions)
SPEC    → business-spec (write requirements in Hebrew)
DESIGN  → technical-spec (write APIs, data model)
TASKS   → to-tickets (vertical slices with dependencies)
BUILD   → ponytail (minimal code) + tdd (test first)
DONE    → code-review (Standards + Spec axes)
```

## Files

```
decisions.md          ← scope + big decisions
business-spec.he.md   ← requirements (Hebrew)
technical-spec.md     ← architecture + APIs
delivery.md           ← tasks + status
```

## Rules

1. **Validate before approve** — run spec-validator, show results
2. **No skipping stages** — each builds on the previous
3. **Changes go back** — re-validate from the changed stage
