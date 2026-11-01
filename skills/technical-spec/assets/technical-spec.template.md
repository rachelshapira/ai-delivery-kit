# Technical Specification — [System]

Template: populate from actual requirements and decisions. Omit or shorten irrelevant sections; do not invent missing targets.

## Baseline
- Status and version/revision:
- Business source baseline:
- Detailed scope:
- Actual technical review/approval reference, when applicable:

## 1. Constraints and architecture
- Organizational standards and constraints:
- Existing reusable capabilities:
- Components, responsibilities, boundaries, and dependencies:
- Main flows and optional diagram:
- Risks affecting delivery order:

## 2. Architectural decision references
| ADR ID | Subject | Register reference |
|---|---|---|

Describe the selected current design here. Keep alternatives, rationale, and decision history in decisions.md.

## 3. Data design
- Entities, relationships, constraints, ownership:
- Lifecycle, history, retention:
- Transactions/concurrency:
- Migration needs:

## 4. API contracts
For each relevant operation:
- REQ/AC references:
- Method/route, request, response:
- Validation and error behavior:
- Authorization and data scope:
- Concurrency/idempotency when relevant:

## 5. Integrations
- Contract, ownership, mapping, authentication:
- Failure, retry, duplicate handling, recovery where needed:

## 6. Security
- Identity and permissions:
- Data scope, audit, sensitive information:

## 7. Client
- Screens, navigation, components, state, API interaction:
- Hebrew text, RTL, accessibility needs:

## 8. Runtime and operations
- Environments/configuration:
- Background work where required:
- Deployment and migrations:
- Monitoring and recovery/rollback where applicable:

## 9. Verification mapping
| REQ/AC | Design reference | Verification approach |
|---|---|---|

## 10. Dependencies and unresolved questions
Reference central question/decision IDs. Do not duplicate their status history.
