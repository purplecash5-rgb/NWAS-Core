# Roadmap

NWAS-Core is an early public framework scaffold. The roadmap below describes
small, reviewable public work; it does not imply a bundled production knowledge
package or included third-party corpus.

## Phase 0: Public scaffold and corpus-safety policy

- Keep the public/private boundary explicit.
- Maintain synthetic-only examples and basic safety checks.
- Document what the public repository will not distribute.

## Phase 1: Source authority model and citation pointer validation

- Define source authority levels and review expectations.
- Validate citation pointer shape without storing third-party source text.
- Add small examples that use toy references only.

## Phase 2: Evidence packet schema and validator examples

- Refine the public evidence packet schema.
- Add compact validator examples for evidence support and review flags.
- Keep generated examples synthetic and clearly labeled.

## Phase 3: Retrieval interface and local LLM layer abstraction

- Document retrieval inputs and outputs as interface contracts.
- Keep the LLM layer model-agnostic and swappable.
- Treat retrieved records as candidates for judgment, not final truth.

## Phase 4: Governance test suite and reproducible audit reports

- Expand tests for corpus safety, schema consistency, and governance rules.
- Add reproducible audit report examples based on synthetic data.
- Keep reports concise enough for code review.

## Phase 5: Optional demo app using synthetic toy corpus only

- Provide a minimal local demo if it helps reviewers understand the flow.
- Use only the toy corpus and synthetic outputs already suitable for public use.
- Avoid implying production readiness or bundled domain knowledge.
