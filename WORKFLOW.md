# Project Workflow

## The Flow

```
SCOPE ──▶ SPEC ──▶ DESIGN ──▶ TASKS ──▶ BUILD ──▶ VERIFY ──▶ DONE ──▶ RELEASE
  │          │         │                            │          │         │
 (provisional)  ✓         ✓                            ○          ○         ✓
              Biz      Tech                       (owner)    (complete)  Deploy
```

## Stages

| # | Stage | Goal | Output | Gate |
|---|-------|------|--------|------|
| 1 | SCOPE | Select what's in/out (provisional) | decisions.md | — |
| 2 | SPEC | Write requirements + ACs | business-spec.he.md | ✅ Business approval |
| 3 | DESIGN | Architecture + APIs | technical-spec.md | ✅ Tech approval |
| 4 | TASKS | Break into work items | delivery.md | — |
| 5 | BUILD | Write code | Code complete | — |
| 6 | VERIFY | Run tests, check ACs | Verification report | — |
| 7 | DONE | ACs and DoD satisfied | Task closed | — |
| 8 | RELEASE | Authorization to deploy | Deployed | ✅ Release approval |

**Three approval gates:** Business (after SPEC), Technical (after DESIGN), Release (when deploying).

**DONE ≠ RELEASE.** A completed task can wait for release.

## Agents

| Agent | Role | Skill |
|-------|------|-------|
| orchestrator | Routes work, manages tasks, tracks state | — |
| spec-agent | Writes business requirements and technical specs | business-spec, technical-spec |
| developer-agent | Implements code following approved REQ/AC | ponytail, tdd |
| verifier-agent | Runs tests, checks ACs and DoD | verification |

## Skills

| Skill | Purpose |
|-------|---------|
| business-spec | Writing requirements in Hebrew |
| technical-spec | Writing architecture, APIs, data model |
| source-extraction | Extracting context from source documents (PDF, DOCX) and existing code |
| ponytail | Implementation simplicity — minimal code to pass tests |
| tdd | Test-first development patterns |
| verification | Run tests, verify ACs and DoD, check standards |
| presentation | Prepare business walkthrough slides and demo scripts |

## UI/UX Responsibility by Stage

| Stage | UI/UX Scope | Where |
|-------|-------------|-------|
| SPEC | User journeys, screens, navigation, actions, fields, validation, permissions, loading/empty/error/success states. Simple wireframes for important flows. | business-spec.he.md + wireframes |
| DESIGN | Component structure, design system usage, responsive behavior, RTL/i18n, accessibility, API integration, client state. | technical-spec.md |
| BUILD | Implement agreed screens using existing components and styles. | Application code |
| VERIFY | Browser behavior against ACs: journeys, validation, permissions, screen sizes, keyboard navigation, RTL. | Verification evidence |

**Business approval after SPEC** must include the important user journeys and wireframes. For new or complex interactions, create a clickable prototype before detailed implementation. Routine screens can follow an already-approved pattern.

**Prototype approach:**
1. Reuse the organization's design system or approved screen patterns, where available.
2. Create a lightweight browser prototype of one representative journey (e.g., list → form → confirmation) using mock data and existing components.
3. Review layout, Hebrew/RTL, navigation, validation, and relevant empty/error states.
4. Record the agreed prototype version in the business specification. Reuse its patterns for subsequent screens.

No separate UX agent or additional approval gate is needed. Include prototype review in the existing business approval after SPEC. Browser verification later checks the implemented result; prototype approval does not prove accessibility or functionality.

**Keep three distinctions clear:**
- **Wireframe** — layout and interaction proposal (for approval)
- **Acceptance criteria** — observable behavior that must work (for verification)
- **Technical design** — how the screen is implemented (belongs in DESIGN)

## Business Walkthrough (Optional)

After a POC or prototype, offer a business walkthrough. This is not a new approval gate — it supports the existing business approval by helping stakeholders understand the solution, see what works, and decide what happens next.

**Format:** Short presentation (5–6 slides) + demo (5 minutes)

| Part | Content |
|------|---------|
| 1. Business need | The problem, users affected, desired outcome |
| 2. Proposed solution | The future business process, what changes for users |
| 3. Demonstration | One realistic journey through the POC with sample data |
| 4. Scope and limitations | What works, what is simulated, what remains unverified |
| 5. Decisions and next steps | Feedback needed, proposed first release, unresolved questions |

**Guidelines:**
- Use actual screenshots and business language
- Explain architecture only when it affects a business decision
- Clearly distinguish: working / simulated / planned functionality
- Aim for 5–6 slides and a 5-minute demo

**Manager responsibilities:**
1. Read the business specification, agreed scope, and POC/prototype verification results
2. Use `presentation` skill to prepare HTML slides and demo script
3. Conduct the walkthrough with stakeholders (open HTML in browser, use F for fullscreen)
4. Record feedback and decisions in `decisions.md`
5. Update affected specifications and next action in `delivery.md`

**Important:** Approval of the POC's direction is not production acceptance. Record exactly what stakeholders agreed to.

For a UI prototype, this walkthrough supports business approval after SPEC. For a technical POC, it informs design and release-scope decisions.

## Files

```
decisions.md          ← scope + decisions
business-spec.he.md   ← requirements (Hebrew)
technical-spec.md     ← architecture + APIs
delivery.md           ← tasks, status, checkpoint
```

## Rules

1. **Business approval covers detailed requirements and ACs.** SCOPE is provisional selection; business gate comes after SPEC.
2. **Reuse valid approvals.** For later increments, revisit only material changes (requirements, ACs, significant design, risk).
3. **DONE means ACs and DoD satisfied.** RELEASE means authorization to deploy. Keep them separate.
4. **One verification owner.** Verification runs tests AND checks ACs/DoD. Failed checks require fixes and re-verification.
5. **Change only the layers needed.** Not every task must be vertical.
6. **Ask questions that affect the next decision.** Record others and continue.

## Validation Checklists

### Before BUSINESS Approval (after SPEC)
- [ ] Problem statement clear
- [ ] In/out scope explicit
- [ ] Every in-scope feature has REQ with testable ACs
- [ ] User roles and permissions defined
- [ ] Blockers resolved (future unknowns OK)

### Before TECHNICAL Approval (after DESIGN)
- [ ] References correct business-spec version
- [ ] Every in-scope REQ has implementation approach
- [ ] No internal contradictions
- [ ] ADRs for non-obvious decisions
- [ ] Security model defined

### Before RELEASE Approval
- [ ] All in-scope ACs verified
- [ ] Verification passed
- [ ] No open blockers
