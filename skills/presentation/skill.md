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
- **Organization branding** — logo file, brand colors

## Branding Guidelines

**CRITICAL:** Presentations must use official organization branding, not project code names.

### Logo
- **Use the real organization logo** — download from official website if needed
- Place logo in `docs/` folder as PNG file (e.g., `btl-logo.png`)
- Reference with relative path: `<img src="logo.png">`
- Header logo: 50px height
- Title slide logo: 100px height
- Thank-you slide: invert colors for dark background (`filter: brightness(0) invert(1)`)

### Title
- **Never use internal project names** (e.g., "NursingPortal") in presentation
- Use the business-facing name in Hebrew (e.g., "פורטל נותני שירותים בסיעוד")
- Subtitle: "סקירה עסקית — שלב X"

### Colors (example: BTL)
```css
:root {
  --primary: #003d79;        /* Main brand blue */
  --primary-light: #0066cc;  /* Lighter blue for accents */
  --accent: #c9a227;         /* Gold for highlights */
  --white: #ffffff;
  --gray: #f8f9fa;           /* Background gray */
}
```

### Header design
- Blue background with organization logo on right
- Gold accent stripe (3px) below header
- Slide title on left in white

## Presentation structure

Create 7 slides following this outline:

### Slide 0: Title
- Organization logo (large, centered)
- Business-facing system name (Hebrew)
- Subtitle: "סקירה עסקית — שלב X"
- Department/unit name
- Organization name

### Slide 1: Business Need
- The problem (highlight box with gold border)
- Two columns:
  - Left: Results/consequences (bullet list)
  - Right: Affected users (card for each role)

### Slide 2: Proposed Solution
- Flow diagram showing process (boxes with arrows)
- Two columns: what changes for each user type

### Slides 3–4: Demonstration
- Feature grid (3 columns × 2 rows)
- Each feature: emoji icon, title, one-line description
- "Open live demo" button linking to prototype

### Slide 5: Scope and Limitations
Table with 3 columns:
| ✅ עובד באב טיפוס | ⚡ מדומה | 🔜 מתוכנן לפיתוח |

Warning box at bottom for untested items.

### Slide 6: Decisions and Next Steps
Two columns:
- Left: Decision box (what's needed from stakeholders) + open questions
- Right: Timeline visualization (numbered circles with connector lines)

### Slide 7: Thank You
- Dark background (primary color)
- Logo (inverted colors)
- "תודה" + "שאלות?"
- Demo links

## Demo script

Prepare a written script for the live demo:

```markdown
## Demo Script: [Feature Name]

**Duration:** ~5 minutes
**Starting point:** [URL or screen]
**Sample data:** [describe test accounts, sample documents, etc.]

### Journey: [Name the journey, e.g., "Provider uploads insurance document"]

1. **[Screen name]** — [Action to perform]
   - Point out: [what to highlight]
   - Say: "[suggested narrative]"

2. **[Next screen]** — [Action]
   - Point out: [highlight]
   - Say: "[narrative]"

[Continue for each step...]

### Edge cases to show (optional)
- Validation error: [how to trigger, what happens]
- Empty state: [how to show]

### Do NOT show
- [List anything broken or confusing that should be avoided]
```

## Language and tone

- Use business language, not technical jargon
- **Never use project code names** — only business-facing names
- Explain architecture only when it affects a business decision
- Use Hebrew for Hebrew-speaking stakeholders
- Reference real business terms from the specification glossary

## After the walkthrough

The manager (not this skill) handles post-walkthrough:
1. Record feedback verbatim in `decisions.md`
2. Distinguish: approved / needs changes / rejected / deferred
3. Update specifications with agreed changes
4. Update `delivery.md` with next action

## Output format

Deliver an **HTML presentation file** — self-contained, opens in browser, navigable with keyboard (arrows/space) and buttons. Supports fullscreen (F key).

The HTML presentation should:
- Use RTL direction for Hebrew content
- Include keyboard navigation (← → or space)
- Support fullscreen mode
- Link to prototype files for live demo
- Be printable (each slide on a page)
- **Use official organization logo** (PNG file, not SVG recreation)
- **Use business-facing name** (not project code name)

```html
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <title>שם המערכת — סקירה עסקית</title>
  <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap" rel="stylesheet">
</head>
<body>
  <div class="slides">
    <div class="slide title-slide" data-slide="0">
      <div class="title-logo"><img src="logo.png" alt="Organization"></div>
      <h1>שם המערכת בעברית</h1>
      <div class="subtitle">סקירה עסקית — שלב 1</div>
      <div class="meta">שם האגף<br>שם הארגון</div>
    </div>
    <div class="slide" data-slide="1"><!-- Business Need --></div>
    <div class="slide" data-slide="2"><!-- Proposed Solution --></div>
    <div class="slide" data-slide="3"><!-- Demo Portal 1 --></div>
    <div class="slide" data-slide="4"><!-- Demo Portal 2 --></div>
    <div class="slide" data-slide="5"><!-- Scope and Limitations --></div>
    <div class="slide" data-slide="6"><!-- Decisions and Next Steps --></div>
    <div class="slide thank-slide" data-slide="7"><!-- Thank You --></div>
  </div>
</body>
</html>
```

Also create a **demo script** (markdown) with step-by-step instructions for the live demo portion.

## Example

For the nursing services provider portal:

**Title slide:**
- Logo: btl-logo.png (downloaded from btl.gov.il)
- Title: "פורטל נותני שירותים בסיעוד" (NOT "NursingPortal")
- Subtitle: "סקירה עסקית — שלב 1"
- Meta: "אגף סיעוד / המוסד לביטוח לאומי"

**Slide 1: Business Need**
> **הבעיה:** נותני שירותים בסיעוד (כ-100 ארגונים, 400 סניפים) מגישים מסמכי התקשרות באופן ידני — פקסים, מיילים, שיחות טלפון.

**Demo script excerpt:**
> 1. **מסך התחברות** — הזן admin@matav.co.il / סיסמה
>    - הצבע על: הממשק בעברית, RTL
>    - אמור: "נות"ש נכנס עם משתמש וסיסמה שהוגדרו לו"
> 
> 2. **לוח בקרה** — הצג את הכרטיסים
>    - הצבע על: 12 מסמכים, 3 ממתינים, 1 דורש תשומת לב
>    - אמור: "במבט אחד הנות"ש רואה את מצב כל המסמכים שלו"
