---
name: verification
description: Single verification owner — run tests, verify ACs and DoD, check coding standards. Combines code inspection with executable checks.
---

# Verification

One verification owner handles both code inspection and executable checks.

## Responsibilities

1. **Run tests** — Execute test suite, report pass/fail
2. **Verify ACs** — Check each acceptance criterion is met
3. **Verify DoD** — Check Definition of Done items
4. **Check standards** — Review code against documented standards
5. **Report evidence** — Provide proof of verification

## Process

### 1. Identify what to verify

From the task or handoff:
- REQ/AC references from spec
- DoD items from delivery.md or project standards
- Files changed (diff from branch point)

### 2. Run executable checks

```bash
# Run test suite
npm test / dotnet test / pytest

# Run linters if configured
npm run lint / dotnet format --verify-no-changes

# Build to catch compile errors
npm run build / dotnet build
```

Record output. All must pass before proceeding.

### 3. Verify each AC

For each acceptance criterion in scope:

| AC | Evidence | Status |
|----|----------|--------|
| AC-001-01 | Test `login.spec.ts:15` passes | ✅ |
| AC-001-02 | Test `login.spec.ts:28` passes | ✅ |
| AC-001-03 | Manual check: filtered by providerId | ✅ |

Evidence types:
- **Test**: Name the test file and line
- **Manual**: Describe what was checked
- **Output**: Quote relevant output

### 4. Browser and accessibility checks

For UI changes, verify in actual browser:
- User journeys work as specified (walk through each flow)
- Validation messages appear correctly
- Error/loading/empty states display properly
- Relevant screen sizes (mobile, tablet, desktop)
- Keyboard navigation (Tab order, Enter/Escape handling)
- RTL layout (if applicable)
- Screen reader basics (labels, ARIA, focus management)

Evidence: Screenshots or recordings for visual behavior; test output for automated a11y checks.

### 5. Check standards

Review diff against:
- `CODING_STANDARDS.md` or equivalent
- `technical-spec.md` patterns section
- Language/framework conventions

Look for:
- Hard violations (cite standard + file:line)
- Code smells (judgement calls, non-blocking)

### 6. Report

```markdown
## Verification Report

**Task:** [ID] — [title]
**Commit:** [sha] (exact commit verified)
**Branch:** [name]
**Environment:** [local / CI / staging — specify]
**Uncommitted changes:** [none / list any — uncommitted changes invalidate verification]

### Tests
- Total: X passed, Y failed, Z skipped
- [List any failures]

### Acceptance Criteria

| AC | Evidence | Status |
|----|----------|--------|
| AC-xxx | [evidence] | ✅ Pass / ❌ Fail / ⚠️ Not verified |

Note: "Not verified" means the criterion could not be checked (missing environment, test not available). This is different from Fail. Missing mandatory evidence prevents Done status.

### DoD
- [ ] Tests pass
- [ ] No lint errors
- [ ] Builds successfully
- [ ] ACs verified

### Standards
- **Violations:** [list or "none"]
- **Judgement calls:** [list or "none"]

### Result
- **Pass** — ready for release approval
- **Fail** — return to developer with: [list issues]
- **Blocked** — verification cannot complete: [reason — missing environment, unavailable test, etc.]
```

## Failure handling

If verification fails:
1. Return to developer with specific issues
2. Developer fixes
3. **Re-run affected checks** — not just the failed ones, but anything the fix might have affected
4. Repeat until pass

## When separate reviewer is optional

Separate additional review is optional only where project policy permits:
- Documentation-only changes
- Config changes with test coverage
- Trivial fixes (typos, formatting)

**Required human approval cannot be waived by an agent.** If project or organizational policy requires human review, that gate must be passed regardless of risk assessment.

**Verification itself is never optional.** Tests must run. ACs must be checked.

## Integration

### Handoff from developer
Developer provides:
- Task ID and REQ/AC references
- Commit or branch to verify
- Evidence of local checks passed
- Any known issues or limitations

### Return to orchestrator
- Task ID
- Verification status (pass/fail)
- Evidence for each AC
- Issues found (if any)
- Next action (release approval / return to developer)
