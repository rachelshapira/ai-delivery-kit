---
name: change-management
description: Standard workflows for updating project documentation with approval gates.
---

# Change Management

## The Four Documents

```
decisions.md          →  WHY we decided (Questions + ADRs)
business-spec.he.md   →  WHAT to build (Requirements + ACs)
technical-spec.md     →  HOW to build (APIs, Data, Tech)
delivery.md           →  WHERE we are (Phase, Tasks, Status)
```

## Approval Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   DISCOVERY          BUSINESS SPEC        TECH SPEC         TASKS       │
│                                                                         │
│   ┌─────────┐        ┌─────────┐         ┌─────────┐      ┌─────────┐  │
│   │ Sources │        │  Draft  │         │  Draft  │      │  Draft  │  │
│   │ Reading │        │ (WHAT)  │         │  (HOW)  │      │ (WORK)  │  │
│   └────┬────┘        └────┬────┘         └────┬────┘      └────┬────┘  │
│        │                  │                   │                 │       │
│        ▼                  ▼                   ▼                 ▼       │
│   ┌─────────┐        ┌─────────┐         ┌─────────┐      ┌─────────┐  │
│   │CHECKPOINT│       │CHECKPOINT│        │CHECKPOINT│     │CHECKPOINT│  │
│   │ "Scope?" │       │"Correct?"│        │"Feasible?"│    │"Ready?"  │  │
│   └────┬────┘        └────┬────┘         └────┬────┘      └────┬────┘  │
│        │                  │                   │                 │       │
│   ┌────┴────┐        ┌────┴────┐         ┌────┴────┐      ┌────┴────┐  │
│   │ Business│        │ Business│         │Technical│      │  Team   │  │
│   │ Approves│        │ Approves│         │ Approves│      │ Approves│  │
│   └────┬────┘        └────┬────┘         └────┬────┘      └────┬────┘  │
│        │                  │                   │                 │       │
│        ▼                  ▼                   ▼                 ▼       │
│   ┌─────────┐        ┌─────────┐         ┌─────────┐      ┌─────────┐  │
│   │decisions│        │business-│         │technical│      │delivery │  │
│   │  .md    │        │spec.he  │         │-spec.md │      │  .md    │  │
│   │ updated │        │ updated │         │ updated │      │ updated │  │
│   └─────────┘        └─────────┘         └─────────┘      └─────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

## Stage Gates

| Stage | Document | Approver | Question | Approved When |
|-------|----------|----------|----------|---------------|
| 1. Scope | decisions.md | Business Owner | "Is this what we want?" | Scope decision recorded |
| 2. Requirements | business-spec.he.md | Business Owner | "Is this correct?" | REQs + ACs approved |
| 3. Design | technical-spec.md | Tech Lead | "Can we build this?" | Architecture approved |
| 4. Tasks | delivery.md | Team | "Ready to start?" | Tasks estimated + assigned |
| 5. Code | (implementation) | Code Reviewer | "Is this good?" | PR approved |
| 6. Done | delivery.md | QA / Business | "Does it work?" | ACs verified |

## Status Values

Each document tracks its status:

```markdown
## פרטי המסמך (in business-spec.he.md)
- **מצב:** טיוטה / בסקירה / מאושר
- **מאשר:** [שם]
- **תאריך אישור:** [תאריך]
```

```markdown
## Baseline (in technical-spec.md)
- **Status:** Draft / In Review / Approved
- **Approved by:** [name]
- **Approval date:** [date]
```

## Change Rules with Approval

| Change Type | Update | Who Approves |
|-------------|--------|--------------|
| Business (what) | business-spec → technical-spec | Business Owner → Tech Lead |
| Technical (how) | technical-spec only | Tech Lead |
| Big tech decision | decisions → technical-spec | Tech Lead (ADR) |
| Scope change | decisions → all docs | Business Owner |

## The Simple Flow

```
1. DISCOVER    →  "Here's what I found. Which scope?"     →  Business approves scope
                                                              ↓
2. SPECIFY     →  "Here are the requirements. Correct?"   →  Business approves REQs
                                                              ↓
3. DESIGN      →  "Here's how to build it. Feasible?"     →  Tech Lead approves design
                                                              ↓
4. PLAN        →  "Here are the tasks. Ready?"            →  Team approves tasks
                                                              ↓
5. BUILD       →  (implement)                             →  Code review approves PR
                                                              ↓
6. VERIFY      →  "Does it meet the ACs?"                 →  QA/Business approves done
```

## Never Skip

❌ Don't write requirements without scope approval  
❌ Don't write technical design without requirements approval  
❌ Don't start coding without design approval  
❌ Don't merge without code review  
❌ Don't mark done without verification  
