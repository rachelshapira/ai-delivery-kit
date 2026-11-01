---
name: technical-spec
description: Create or refine English architecture and technical design from business requirements and organizational standards. Use for initial architecture, detailed implementation design, and technical change-impact assessment.
---

# Technical Specification

## Baseline and template
Read relevant business requirements and approval status, accepted decisions, standards, and existing code/capabilities. Link design to REQ IDs. When creating the document, read [technical template](assets/technical-spec.template.md). Copy to the configured project path; do not create competing documents.

## Work at the requested depth
Initial architecture identifies components, responsibilities, boundaries, shared capabilities, integrations, dependencies, constraints, and material risks. It supports delivery planning without fixing every future detail.

Detailed design covers the selected scope sufficiently for implementation. Label design based on unresolved requirements provisional. Surface significant decisions for technical-owner review; routine details within accepted constraints do not need another approval ceremony.

## Design content
Cover as applicable:
- Technology choices and standards.
- Module responsibilities and dependency direction.
- Entities, relationships, constraints, history, and lifecycle.
- API operations, request/response shapes, validation, and errors.
- Authentication, authorization enforcement, and data scope.
- Transactions, concurrent updates, background work, retries, and idempotency.
- External contracts, mapping, ownership, authentication, and failure recovery.
- Client structure, state, navigation, and server interaction.
- Configuration, deployment, monitoring, backup/recovery, and migrations.
- Verification approach, integration risks, and requirement mapping.

Load technology skills on demand. Verify changing technical facts against authoritative documentation when they affect a decision.

## Decisions and simplicity
Propose significant ADRs to the orchestrator with context, decision, real alternatives, rationale, consequences, and affected scope. It records them centrally. Reference accepted ADRs; describe the resulting current design here without copying decision history.

Prefer existing capabilities and the simplest sufficient design. Justify extra services, queues, caches, generic engines, or databases with concrete needs. Do not fully design deferred scope. Use diagrams where they clarify relationships or complex flows.

## Business alignment
Never alter business behavior to simplify implementation. Return gaps or proposed scope changes to the orchestrator. If it is an English translation ambiguity, return to the Hebrew source; request clarification if needed.

Ensure selected requirements have implementation and verification approaches. Include operational implications when the change requires them, not as universal boilerplate.

## Return
Return changed design sections, affected REQ IDs, proposed questions/ADRs, baseline, dependencies, and readiness. Edit only assigned design artifacts; shared decision/delivery updates belong to the orchestrator.
