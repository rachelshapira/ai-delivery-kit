# Package checks — v1.1

Date: 2026-11-01

## Performed
- Parsed YAML frontmatter for all six SKILL.md files: required name/description and matching folder names.
- Checked local Markdown links and linked template destinations.
- Confirmed five agent prompts, six skills, and four canonical project templates.
- Reviewed the full bundle independently for lifecycle contradictions, template ownership, approval boundaries, evidence freshness, tracker ownership, question incorporation, and runtime-portability claims.
- Clarified manual skill loading and the manual independent-verification path following review.
- Added code-review skill adapted from Matt Pocock's skills repo (two-axis Standards/Spec review).
- Checked UTF-8 readability and final ZIP integrity.

The orchestrator prompt is approximately 487 whitespace-separated words. This is a size measurement, not a model-token estimate or a guarantee about host context use.

## Scope and limits
These checks validate package structure and instruction consistency. They are not a live execution test of agents, an installed skill, a CI gate, or a native runtime integration.

No application was implemented, no user environment was configured, and no live workflow success is claimed. Use examples/lifecycle-check.he.md in the target host to validate actual delegation, tools, persistence, permissions, and evidence handling.

Templates intentionally contain empty fields and example identifiers. They are not actual approvals, requirements, tasks, or test results.
