# Research Profile Contract

A research profile is a public contract for a retrieval or research mode. It
describes what a knowledge assistant is allowed to query, how far it may
iterate, what it may export, and what audit trail should be preserved.

The contract is intentionally separate from private runtime configuration. It
does not include credentials, private source locations, proprietary corpus
records, evidence packets, generated reports, indexes, or deployment settings.

## Why Profiles Matter

Source-governed assistants need explicit boundaries. A profile gives reviewers
and implementers a compact way to inspect:

- The intended use case for a retrieval mode.
- Which connector types are permitted.
- Whether network access is required.
- How many iterations and results are allowed.
- Which exports are available.
- What caution notes and audit expectations apply.

This makes retrieval behavior easier to compare, test, and review before a
system is connected to any real corpus.

## Fast and Deep Profiles

Fast or default profiles should use lower iteration counts, fewer questions per
iteration, and smaller result caps. They are suitable for quick triage,
lightweight summarization, or checking whether a question has enough support to
continue.

Deep or full profiles may allow more iterations, broader connector coverage,
and larger result caps. They should also require stronger audit expectations,
clearer export traceability, and explicit caution for medical, legal, financial,
or other high-stakes topics.

## Auditability

A profile helps make retrieval behavior auditable by turning operational limits
into reviewable data. An implementation can record the active profile ID,
allowed connector types, iteration counts, result limits, and export format for
each governed answer or evidence packet.

Profiles do not prove that a result is correct. They make it easier to inspect
whether the assistant stayed inside declared retrieval boundaries.

## Export Traceability

Exports should preserve traceability from final answer back to the retrieval
profile and source pointers used to produce it. A governed export should retain:

- The profile identifier.
- The export format.
- Source connector types used.
- Citation or evidence pointers.
- Review flags and limitations.

Exports should not remove provenance fields merely to make an answer look
simpler.

## Public Safety Boundary

NWAS-Core includes only public framework contracts and synthetic examples. It
does not include private corpus material, real third-party content, private
research outputs, real evidence packets, private profile configuration,
indexes, deployable data stores, or model artifacts.

Profiles in this repository are examples only. Example source names such as
`scholarly_index`, `preprint_index`, `repository_search`, and
`local_toy_corpus` are synthetic or generic labels, not references to private
systems.
