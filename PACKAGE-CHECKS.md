# Package checks — v1.1

Date: 2026-11-02
Commit: 6b50c1c

## Contents

**Agents (4):**
- orchestrator.md
- spec-agent.md
- developer-agent.md
- verifier-agent.md

**Skills (7):**
- business-spec
- technical-spec
- verification
- source-extraction
- presentation
- tdd
- ponytail

**Templates (4):**
- skills/business-spec/assets/business-spec.he.template.md
- skills/technical-spec/assets/technical-spec.template.md
- templates/delivery.template.md
- templates/decisions.template.md

**Scripts (1):**
- scripts/extract-pdfs.py

## Performed

- Verified all seven SKILL.md files exist with valid YAML frontmatter (name/description).
- Checked local Markdown links point to existing files.
- Confirmed four agent prompts reference correct skills.
- Verified two templates exist in `templates/` folder.
- Confirmed extract-pdfs.py script exists in `scripts/`.
- Reviewed verification skill supports Blocked status and Not verified per-criterion.
- Confirmed verifier-agent handoff includes BLOCKED status.
- Verified decision ownership: spec-agent proposes, manager records.
- Confirmed orchestrator startup handles missing delivery.md and reconciliation.

## Scope and limits

These checks validate package structure and instruction consistency. They are not a live execution test of agents, an installed skill, a CI gate, or a native runtime integration.

No application was implemented, no user environment was configured, and no live workflow success is claimed. Use examples/lifecycle-check.he.md in the target host to validate actual delegation, tools, persistence, permissions, and evidence handling.

Templates intentionally contain empty fields and example identifiers. They are not actual approvals, requirements, tasks, or test results.
