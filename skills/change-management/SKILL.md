---
name: change-management
description: Standard workflow for project documentation with validation and approval gates.
---

# Change Management

## The Flow

```
DISCOVER → VALIDATE → APPROVE → SPECIFY → VALIDATE → APPROVE → DESIGN → VALIDATE → APPROVE → PLAN → VALIDATE → APPROVE → BUILD → REVIEW → VERIFY → DONE
```

## Simple Version

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ DISCOVER │ ──▶ │ SPECIFY  │ ──▶ │  DESIGN  │ ──▶ │   PLAN   │ ──▶ BUILD
│  scope   │     │   what   │     │   how    │     │   tasks  │
└────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘
     │                │                │                │
     ▼                ▼                ▼                ▼
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│ VALIDATE │     │ VALIDATE │     │ VALIDATE │     │ VALIDATE │
│ + APPROVE│     │ + APPROVE│     │ + APPROVE│     │ + APPROVE│
│ Business │     │ Business │     │ Tech Lead│     │   Team   │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
     │                │                │                │
     ▼                ▼                ▼                ▼
 decisions.md    business-spec    technical-spec    delivery.md
```

## Each Stage

### 1. DISCOVER → decisions.md

**Do:** Read sources, list all processes, ask scope questions  
**Validate:** All processes listed? Scope decision clear?  
**Approve:** Business Owner — "Is this the scope we want?"  
**Output:** Scope recorded in `decisions.md`

---

### 2. SPECIFY → business-spec.he.md

**Do:** Write REQs and ACs for in-scope processes  
**Validate:** Every process has REQs? Every REQ has ACs? ACs testable?  
**Approve:** Business Owner — "Are the requirements correct?"  
**Output:** Status = "מאושר" in `business-spec.he.md`

---

### 3. DESIGN → technical-spec.md

**Do:** Write architecture, APIs, data model, verification mapping  
**Validate:** Every REQ has API? Every AC has test approach? ADRs incorporated?  
**Approve:** Tech Lead — "Can we build this?"  
**Output:** Status = "Approved" in `technical-spec.md`

---

### 4. PLAN → delivery.md

**Do:** Break into tasks, estimate, assign, order by dependency  
**Validate:** Every REQ covered? Estimates done? Dependencies clear?  
**Approve:** Team — "Ready to start?"  
**Output:** Tasks listed in `delivery.md`

---

### 5. BUILD → code

**Do:** Implement tasks  
**Review:** Code reviewer — "Is this good code?"  
**Verify:** QA/Business — "Does it meet the ACs?"  
**Output:** PR merged, AC verified

---

## The Four Documents

| Document | Contains | Updated At | Approved By |
|----------|----------|------------|-------------|
| `decisions.md` | Scope, Questions, ADRs | Discover | Business |
| `business-spec.he.md` | REQs, ACs (Hebrew) | Specify | Business |
| `technical-spec.md` | APIs, Data, Tech | Design | Tech Lead |
| `delivery.md` | Phase, Tasks, Status | Plan | Team |

## Validation Checklist (Quick)

Before each approval, check:

| Stage | Must Have |
|-------|-----------|
| Scope | All processes listed, in/out decided |
| Business Spec | REQs + ACs for all in-scope, testable |
| Technical Spec | API for each REQ, test for each AC |
| Tasks | Task for each REQ, estimates, dependencies |

## Change Rules

| Change Type | Update | Validate | Approve |
|-------------|--------|----------|---------|
| Business (what) | business-spec → technical-spec | Both | Business → Tech |
| Technical (how) | technical-spec | Technical only | Tech Lead |
| Scope change | decisions → all | All | Business |

## Never Skip

❌ No approval without validation  
❌ No next stage without approval  
❌ No code without approved design  
❌ No merge without review  
❌ No done without verification
