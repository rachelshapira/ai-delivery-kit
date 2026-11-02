---
name: business-functional-spec
description: Create, review, and improve professional Hebrew Business Functional Specification documents (מסמך אפיון פונקציונלי עסקי) for enterprise information systems. Use when transforming business requirements, meeting notes, existing documents, or stakeholder input into structured, traceable, business-approval-ready specifications.
---

# Business Functional Specification

## Objective
Create a professional, complete, consistent, and understandable Business Functional Specification (BFS) suitable for review and formal approval by business stakeholders.

The document must explain WHAT the system does, WHO uses it, HOW business processes operate, and WHICH rules govern them.

Do not turn the document into a technical design.

## Language and Audience
- Write in professional, clear Hebrew.
- Use terminology understood by business users and operational managers.
- Use RTL formatting in generated Word documents.
- Avoid implementation details unless needed to clarify business behavior.
- Use one consistent term for each business concept.
- Explain abbreviations at first use.
- Prefer precise, short sentences over vague or overly formal language.

## Source Analysis
Before drafting:
1. Read every supplied source.
2. Identify business objectives, actors, processes, entities, rules, reports, and interfaces.
3. Extract explicit requirements and their sources.
4. Identify contradictions, duplications, missing information, and assumptions.
5. Classify every item as Confirmed, Proposed, Unclear, or Out of Scope.
6. Do not invent requirements to fill gaps.
7. Ask focused clarification questions for critical ambiguities.
8. Preserve important details from original sources.

## Required Document Structure
Adapt the following structure to the complexity of the system. Do not add empty chapters merely to follow a template.

1. Cover Page and Document Control
   - System name
   - Document title
   - Version, date, owner
   - Business stakeholders
   - Status and approval information
   - Version history

2. Purpose and Background
   - Business problem
   - Objectives
   - Expected business value
   - Current situation and main pain points

3. Executive Summary
   - High-level system description
   - Main business processes
   - Business users
   - Main expected outcomes

4. Scope and Boundaries
   - In-scope capabilities
   - Out-of-scope capabilities
   - Phase/MVP boundaries when applicable
   - Dependencies and assumptions
   - Module-to-requirement mapping

5. Business Roles and Responsibilities
   - Role definitions
   - Organizational scope
   - Main responsibilities
   - Permissions at business level

6. Organizational Structure and Core Entities
   - Relevant organizational hierarchy
   - Main business objects
   - Ownership and relationships
   - Business data ownership and source of truth

7. Business Modules and Processes
   - Organize by business capability and process, not by technical component.
   - Assign sequential section numbers and stable requirement IDs.
   - Use the process definition template below.

8. Cross-Cutting Business Capabilities
   - Search and filtering
   - Notifications and reminders
   - Documents and attachments
   - Audit history
   - Authorization
   - Dashboards and reports
   - Other shared capabilities relevant to the scope

9. External Systems and Business Interfaces
   - External system
   - Business purpose
   - Information exchanged
   - Direction and triggering event
   - Ownership and business expectations
   - Exception behavior where relevant
   - Do not specify protocols, endpoints, or database schemas unless explicitly requested.

10. Reports and Management Information
   - Report name and purpose
   - Intended audience
   - Filters and data
   - Frequency
   - Export or distribution requirements

11. Business Acceptance Criteria
   - Critical business scenarios
   - Expected outcomes
   - Validation and rejection cases
   - Acceptance responsibility

12. Open Issues and Decisions
   - Decision ID
   - Issue
   - Business impact
   - Proposed options where relevant
   - Decision owner
   - Status
   - Required date, when known

13. Approval
   - Approvers and roles
   - Approval scope
   - Approval status
   - Date and comments

Appendices
   - Source-to-requirement traceability matrix
   - Relevant business catalogs and reference tables
   - Supporting process diagrams
   - Source document list

## Process Definition Template
For each major business process, document:

### Process Name and Identifier
- Purpose and business outcome
- Trigger
- Actors and responsibilities
- Preconditions
- Main flow as numbered business steps
- Alternative flows
- Exceptions and rejection scenarios
- Business rules
- Relevant information and documents
- States and transitions when applicable
- Notifications and outputs
- Authorization and approval requirements
- Dependencies on external systems
- Acceptance criteria
- Open decisions

Only include fields relevant to the process. Keep simple processes concise.

## Requirement Quality
Each important requirement must be:
- Clear and unambiguous
- Business-oriented
- Testable
- Traceable to its source
- Consistent with related processes
- Identifiable by a stable requirement ID

Use precise wording such as:
"המערכת תאפשר למנהל האזור לאשר או לדחות בקשה."
Avoid vague wording such as:
"המערכת תנהל בקשות בצורה חכמה ויעילה."

Where relevant, describe:
- Who may perform the action
- Under what conditions
- What changes as a result
- What happens when validation fails

Do not invent numeric thresholds, deadlines, permissions, or calculations.

## Diagrams
Add diagrams only when they improve understanding.

Prefer:
- Business process flowcharts for multi-step workflows
- Swimlane diagrams for processes involving multiple roles
- State diagrams for complex lifecycle transitions
- High-level business entity diagrams for important relationships

Every diagram must agree with the written specification.
Do not use infrastructure or software architecture diagrams in a business specification unless specifically requested.

## Business Rules
Document significant business rules explicitly.
Prefer stable identifiers such as BR-001.

A rule should state:
- The condition
- The required system behavior
- Relevant actors or roles
- Exceptions
- Source or approval status

Separate confirmed rules from proposed rules.

## Traceability
Maintain a source-to-requirement mapping.

For each original requirement:
- Source and source reference
- Requirement ID
- Specification section
- Coverage status

Coverage statuses:
- Covered
- Partially Covered
- Pending Clarification
- Out of Scope

Do not silently omit any source requirement.

## Approval Readiness
Before declaring the document ready for business approval, verify:

1. All in-scope modules are described.
2. Every key process has a complete and understandable flow.
3. Business roles and responsibilities are clear.
4. Business rules are explicit and noncontradictory.
5. Critical exceptions are covered.
6. Important requirements have acceptance criteria.
7. Interfaces and external dependencies are identified.
8. Open decisions are visible, with business owners where known.
9. Scope and exclusions are clear.
10. Source requirements are traceable.
11. No unapproved assumption is presented as confirmed fact.
12. The document can be understood by business stakeholders without a developer explaining it.

Distinguish between:
- Ready for Business Review
- Ready for Approval with Explicit Open Items
- Not Ready for Approval
- Approved

Never mark a document Approved without actual approval evidence.
If a substantial change is made after approval, mark the revised version as pending approval or follow the organization's change-control process.

## Consistency Validation
After EVERY document update:

1. Compare the scope table with detailed sections.
2. Check numbering and stable requirement IDs.
3. Verify all cross-references.
4. Confirm consistent terminology.
5. Check role definitions against process permissions.
6. Check business rules against process descriptions.
7. Confirm diagrams match the written flows.
8. Verify acceptance criteria for significant requirements.
9. Reconcile traceability to the source requirements.
10. Update version history and approval status.
11. Detect duplicates and contradictions.
12. Preserve unaffected requirements and decisions.

Report unresolved problems with severity and location.
Never claim validation passed without performing the check.

## Document Presentation
When generating a Word document:
- Use a professional cover page.
- Include an automatically generated table of contents where supported.
- Use consistent heading styles and section numbering.
- Use RTL paragraphs and tables for Hebrew content.
- Use readable typography and restrained colors.
- Repeat table headers across pages.
- Avoid excessive blank space and unnecessary page breaks.
- Prevent orphan headings and broken tables.
- Use consistent page headers, footers, and page numbering.
- Render and visually inspect the final document when tools permit.

## Review Output
When asked to review an existing specification, provide:

1. Overall approval-readiness assessment.
2. Critical gaps that prevent approval.
3. Important improvements.
4. Minor editorial or formatting issues.
5. Specific recommended changes.
6. A clear final verdict.

Do not rewrite the entire document unless requested.

## Final Quality Gate
A document is ready for business approval only when:
- Its purpose and scope are understood.
- Stakeholders can validate expected system behavior.
- Important business decisions are explicit.
- Significant requirements are testable and traceable.
- Critical ambiguities are resolved or explicitly excluded from approval.
- Structure, terminology, and references are internally consistent.

Favor clarity and business completeness over document length.
