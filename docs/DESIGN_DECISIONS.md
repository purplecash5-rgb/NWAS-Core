# Design Decisions

## Decision 001: Public repo contains framework only

Status: Accepted

NWAS-Core will publish framework guidance, schemas, validation logic, interface
contracts, and synthetic examples only. Real data layers remain private.

This keeps the public repository useful for architecture review and open-source
collaboration while avoiding disclosure of private knowledge assets, profile
records, governed answer datasets, corpus-derived evidence, or deployment data
stores.

Consequences:

- Public examples must be synthetic.
- Public schemas should describe contracts without requiring private records.
- Tests should scan for accidental private data artifacts before release.
- Downstream users must supply and govern their own lawful corpora.

## Decision 002: LLM layer remains model-agnostic and swappable

Status: Accepted

The LLM layer is an optional drafting and suitability-judging component. Public
interfaces should not depend on a specific model, runtime, vendor, checkpoint,
or deployment style.

Consequences:

- Schemas should describe inputs, outputs, and review metadata rather than a
  model-specific protocol.
- Documentation may mention local-first operation, but must not require one
  concrete model.
- Validators should evaluate governed output behavior, not model identity.

## Decision 003: Retrieval results are evidence candidates

Status: Accepted

Retrieval output is not automatic answer truth. Retrieved items are candidates
that must be judged for source authority, relevance, profile fit, citation
quality, and governance constraints before they support an answer.

Consequences:

- Evidence packet examples should distinguish candidate retrieval from accepted
  support.
- Weak or irrelevant matches should be rejectable.
- Answer drafting remains subordinate to evidence and validation.
