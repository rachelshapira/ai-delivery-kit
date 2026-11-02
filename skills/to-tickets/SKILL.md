---
name: to-tickets
description: Break a spec into vertical-slice tickets with blocking edges. Use at TASKS stage.
source: https://github.com/mattpocock/skills
---

# To Tickets

Break a spec into **tracer-bullet tickets**: vertical slices that cut through all layers.

## Vertical Slice Rules

- Each slice cuts a COMPLETE path through every layer (schema, API, UI, tests)
- A completed slice is demoable or verifiable on its own
- Each slice fits in a single context window
- Prefactoring should be done first

## Process

1. **Read** the spec to understand what needs to be built
2. **Explore** codebase to use project vocabulary and respect ADRs
3. **Draft** vertical slices with blocking edges
4. **Quiz** user: granularity right? edges correct? split/merge needed?
5. **Publish** tickets after user approves

## Ticket Format

```markdown
# <NN>: <Ticket title>

**What to build:** end-to-end behaviour from user's perspective

**Blocked by:** tickets that must complete first, or "None"

**Status:** ready

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2
```

## Rules

- Avoid file paths or code snippets (they go stale)
- Number in dependency order (blockers first)
- Each ticket declares what blocks it
