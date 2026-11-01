---
name: code-review
description: Two-axis review of code changes — Standards (does it follow repo conventions and smell baseline?) and Spec (does it match the originating requirements?). Use after developer handoff and before QA verification.
---

# Code Review

Two-axis review of the diff between `HEAD` and a fixed point:

- **Standards**: Does the code conform to documented coding standards and avoid code smells?
- **Spec**: Does the code faithfully implement the originating requirements/AC?

Both axes run as **parallel independent reviews** to prevent one from masking the other.

## Why two axes

A change can pass one axis and fail the other:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail**
- Code that does exactly what the issue asked but breaks conventions → **Spec pass, Standards fail**

Reporting them separately stops one axis from contaminating the other.

## Process

### 1. Pin the fixed point

Identify the comparison target (commit SHA, branch, tag, `main`, `HEAD~N`). Use three-dot diff for merge-base comparison:

```
git diff <fixed-point>...HEAD
git log <fixed-point>..HEAD --oneline
```

Confirm the ref resolves and the diff is non-empty before proceeding.

### 2. Identify the spec source

Look for the originating spec in order:
1. Issue references in commit messages (`#123`, `Closes #45`, REQ-xxx, AC-xxx)
2. Linked task in `delivery.md` with REQ/AC references
3. Path passed by orchestrator/user
4. Spec file under `docs/` matching branch/feature name

If no spec exists, run Standards-only review and note "no spec available".

### 3. Identify standards sources

Collect all files documenting how code should be written:
- `CODING_STANDARDS.md`, `CONTRIBUTING.md`
- `docs/technical-spec.md` patterns section
- Language/framework style guides referenced in project

### 4. Smell baseline (always applies)

These Fowler code smells apply universally unless a documented repo standard explicitly overrides them. Each is a **judgement call**, not a hard violation:

| Smell | What it is | How to fix |
|-------|-----------|------------|
| **Mysterious Name** | Name doesn't reveal purpose | Rename; if no honest name, design is murky |
| **Duplicated Code** | Same logic shape in multiple places | Extract shared shape, call from both |
| **Feature Envy** | Method reaches into another object's data more than its own | Move method to the data it envies |
| **Data Clumps** | Same fields/params travel together | Bundle into one type |
| **Primitive Obsession** | Primitive standing in for domain concept | Give concept its own type |
| **Repeated Switches** | Same switch/if-cascade recurs | Replace with polymorphism or shared map |
| **Shotgun Surgery** | One change forces scattered edits | Gather what changes together |
| **Divergent Change** | One file edited for unrelated reasons | Split by reason for change |
| **Speculative Generality** | Abstraction for needs spec doesn't have | Delete until real need shows |
| **Message Chains** | Long `a.b().c().d()` navigation | Hide walk behind one method |
| **Middle Man** | Class mostly just delegates | Cut it, call target direct |
| **Refused Bequest** | Subclass ignores/overrides most inherited | Drop inheritance, use composition |

### 5. Run both reviews

**Standards review** checks:
- Documented standard violations (cite file + rule)
- Smell baseline findings (name smell, quote hunk)
- Distinguish hard violations from judgement calls
- Skip anything tooling already enforces

**Spec review** checks:
- Requirements missing or partial (quote spec line)
- Behavior not asked for (scope creep)
- Requirements implemented incorrectly (quote spec line)

### 6. Aggregate and report

Present findings under separate headings:

```markdown
## Standards

### Violations (blocking)
- [file:line] Violates [standard]: [description]

### Judgement calls (non-blocking)
- [file:line] Possible [smell]: [description]

## Spec

### Missing requirements
- REQ-xxx: [requirement] — not implemented / partially implemented

### Scope creep
- [file:line] Adds [behavior] not in spec

### Incorrect implementation
- REQ-xxx / AC-xxx: [expected] vs [actual]

## Summary
- Standards: X violations, Y judgement calls
- Spec: X missing, Y creep, Z incorrect
- Worst Standards issue: [description]
- Worst Spec issue: [description]
- Blocking: Yes/No
```

Do **not** merge or rerank findings across axes.

## Integration with delivery kit

### Workflow position
```
Developer (Ready for verification)
    ↓
Code Reviewer ← you are here
    ↓
QA Agent (behavioral verification)
    ↓
Human review (if required)
    ↓
Done
```

### Return to orchestrator
- Task ID and scope reviewed
- Candidate identity (commit + build if available)
- Standards findings with severity
- Spec findings with REQ/AC references
- Blocking classification
- Next action (proceed to QA / return to developer / needs decision)

### Blocking rules
- Any Standards violation → blocks
- Any Spec "missing requirement" for AC in scope → blocks
- Judgement calls alone → does not block, but noted

### What this is NOT
- Not QA: does not run tests or verify runtime behavior
- Not approval: does not replace human code review where required
- Not implementation: does not fix issues, only reports them
