---
name: presentation
description: Prepare business walkthrough presentations and demo scripts for POCs and prototypes. Creates stakeholder-ready slides and realistic demo flows.
---

# Presentation

Prepare concise presentations for business walkthroughs after POCs or prototypes.

## When to use

- After UI prototype completion, before business approval
- After technical POC, to inform design decisions
- When stakeholders need to see and decide on a solution direction

## Inputs required

Before preparing the presentation, gather:
- Business specification (problem, users, scope)
- Prototype or POC artifacts (screenshots, working URLs)
- Verification results (what was tested, what passed)
- Open questions and decisions needed from `decisions.md`
- Current delivery status from `delivery.md`
- Organization branding — logo file, brand colors

## Presentation structure

Create 6 content slides (0–5 index) following this outline:

### Slide 0: Title
- Organization logo (large, centered)
- Business-facing system name (use glossary term, not code name)
- Subtitle: "סקירה עסקית — שלב X"
- Department/unit name
- Organization name

### Slide 1: Business Need
- The problem (highlight box)
- Two columns:
  - Results/consequences (bullet list)
  - Affected users (card for each role)

### Slide 2: Proposed Solution
- Flow diagram showing process (boxes with arrows)
- Two columns: what changes for each user type

### Slide 3: Demonstration
- Feature grid (3 columns × 2 rows)
- Each feature: icon, title, one-line description
- "Open live demo" button linking to prototype

### Slide 4: Scope and Limitations
Table with 3 columns:
| ✅ Working in prototype | ⚡ Simulated | 🔜 Planned |

Note box at bottom listing untested items and known limitations.

### Slide 5: Decisions and Next Steps
- Decision box (what's needed from stakeholders)
- Open questions requiring business input

## Demo script

Prepare a written script for the live demo:

```markdown
## Demo Script: [Feature Name]

**Duration:** ~5 minutes
**Starting point:** [URL or screen]
**Sample data:** [describe test accounts, sample documents, etc.]

### Journey: [Name the journey]

1. **[Screen name]** — [Action to perform]
   - Point out: [what to highlight]
   - Say: "[suggested narrative]"

2. **[Next screen]** — [Action]
   - Point out: [highlight]
   - Say: "[narrative]"

### Known limitations
- [List limitations that affect stakeholder decisions]
- [Keep demo focused; disclose what matters for the decision]
```

## Language and tone

- Use business language, not technical jargon
- Never use project code names — only business-facing names from the glossary
- Explain architecture only when it affects a business decision
- Use the stakeholder's language (Hebrew for Hebrew-speaking stakeholders)
- Reference real business terms from the specification glossary

## After the walkthrough

The manager (not this skill) handles post-walkthrough:
1. Record feedback verbatim in `decisions.md`
2. Distinguish: approved / needs changes / rejected / deferred
3. Update specifications with agreed changes
4. Update `delivery.md` with next action

## Output format

Deliver:
1. **HTML presentation file** with navigation (keyboard arrows/space, fullscreen F key)
2. **Demo script** (markdown) with step-by-step instructions
3. **Assets folder** containing logo and any required images

### Asset handling

Presentations require external assets (logo, images). Deliver as a folder:
```
docs/walkthrough/
├── index.html          # The presentation
├── demo-script.md      # Demo instructions
└── assets/
    └── logo.png        # Organization logo
```

Or embed assets as base64 data URIs for true single-file delivery.

For fonts: either embed as base64, use system fonts, or document the Google Fonts dependency.

### HTML structure

```html
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <title>[System name] — סקירה עסקית</title>
  <!-- Font: embed, system fallback, or external with documented dependency -->
</head>
<body>
  <div class="slides">
    <div class="slide" data-slide="0"><!-- Title --></div>
    <div class="slide" data-slide="1"><!-- Business Need --></div>
    <div class="slide" data-slide="2"><!-- Proposed Solution --></div>
    <div class="slide" data-slide="3"><!-- Demonstration --></div>
    <div class="slide" data-slide="4"><!-- Scope and Limitations --></div>
    <div class="slide" data-slide="5"><!-- Decisions and Next Steps --></div>
  </div>
</body>
</html>
```

## Branding

Apply organization branding consistently:
- Use official logo (download from official source if needed)
- Match brand colors from style guide
- Use business-facing system name, not internal code names

---

## Reference: Example styling

For organizations requiring specific styling (e.g., government agencies), create a separate style reference document. The core skill remains reusable across projects.
