---
name: change-management
description: Standard workflows for updating project documentation. Simple rules for what goes where.
---

# Change Management

## The Four Documents

```
┌─────────────────────────────────────────────────────────────────┐
│                        decisions.md                             │
│                    "WHY we decided"                             │
│              Questions (Q-XXX) + Decisions (ADR-XXX)            │
└─────────────────────┬───────────────────────────────────────────┘
                      │ feeds into
                      ▼
┌────────────────────────────────┐    ┌──────────────────────────┐
│      business-spec.he.md       │    │    technical-spec.md     │
│        "WHAT to build"         │───▶│     "HOW to build"       │
│    Requirements (REQ-XXX)      │    │   APIs, Data, Tech Stack │
│  Acceptance Criteria (AC-XXX)  │    │                          │
└────────────────────────────────┘    └──────────────────────────┘
                      │                          │
                      └────────────┬─────────────┘
                                   ▼
                      ┌──────────────────────────┐
                      │       delivery.md        │
                      │    "WHERE we are"        │
                      │   Phase, Tasks, Status   │
                      └──────────────────────────┘
```

## One Simple Rule

| Type of Change | Where to Update |
|----------------|-----------------|
| **Business** (features, rules, Hebrew text) | `business-spec.he.md` → then `technical-spec.md` |
| **Technical** (database, framework, APIs) | `technical-spec.md` only |
| **Big technical decision** (new DB, new framework) | `decisions.md` (ADR) → then `technical-spec.md` |
| **Question answered** | `decisions.md` → then affected spec |
| **Scope change** | `decisions.md` → both specs → `delivery.md` |

## Flow Chart

```
┌─────────────────────────────────┐
│     What kind of change?        │
└───────────────┬─────────────────┘
                │
    ┌───────────┼───────────┬─────────────┐
    ▼           ▼           ▼             ▼
┌────────┐ ┌────────┐ ┌──────────┐ ┌───────────┐
│Business│ │Technical│ │ Question │ │   Scope   │
│ rule/  │ │  (how)  │ │ answered │ │  change   │
│feature │ │         │ │          │ │           │
└───┬────┘ └───┬────┘ └────┬─────┘ └─────┬─────┘
    │          │           │             │
    ▼          ▼           ▼             ▼
┌────────┐ ┌────────┐ ┌──────────┐ ┌───────────┐
│business│ │technical│ │decisions │ │ decisions │
│-spec.he│ │-spec.md │ │   .md    │ │   .md     │
└───┬────┘ └────────┘ └────┬─────┘ └─────┬─────┘
    │                      │             │
    ▼                      ▼             ▼
┌────────┐           ┌──────────┐ ┌───────────┐
│technical│          │ affected │ │both specs │
│-spec.md │          │   spec   │ │+ delivery │
└────────┘           └──────────┘ └───────────┘
```

## Examples

| I want to... | Do this |
|--------------|---------|
| Add "expiry date" to documents | business-spec.he.md (add to REQ) → technical-spec.md (add field) |
| Switch to MongoDB | decisions.md (add ADR) → technical-spec.md (update §1, §3) |
| Add a validation rule | business-spec.he.md (add AC) → technical-spec.md (add to API) |
| Change API response format | technical-spec.md only |
| Legacy integration decided | decisions.md (answer Q-TECH-001) → technical-spec.md (§5) |
| Add PROC-05 to Phase 1 | decisions.md → business-spec.he.md → technical-spec.md → delivery.md |

## Never Do This

❌ Change code without updating spec first  
❌ Put technical details in business-spec.he.md  
❌ Put business rules in technical-spec.md  
❌ Make big tech decisions without ADR in decisions.md  
❌ Change scope without updating delivery.md
