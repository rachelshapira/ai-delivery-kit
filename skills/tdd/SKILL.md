---
name: tdd
description: Test-driven development with red-green loop. Use when building features or fixing bugs test-first.
---

# Test-Driven Development

Red → Green loop. One test, one implementation, repeat.

## Rules

1. **Red first**: Write a failing test before any implementation
2. **Green minimal**: Write only enough code to pass the test
3. **One slice at a time**: One AC → one test → one implementation
4. **Test behavior, not implementation**: Tests should survive refactors

## What makes a good test

- Tests public interfaces, not internals
- Expected values come from the spec/AC, not from copying the code logic
- Reads like a specification: "user can checkout with valid cart"

## Anti-patterns to avoid

- **Implementation-coupled**: Breaks when you refactor but behavior didn't change
- **Tautological**: `expect(add(a,b)).toBe(a+b)` — proves nothing
- **All tests first**: Write one test, implement, repeat — not bulk tests then bulk code

## Process

1. Pick one AC
2. Write a failing test for it
3. Run it — confirm it fails (red)
4. Write minimal code to pass
5. Run it — confirm it passes (green)
6. Next AC

Done when all AC have passing tests.
