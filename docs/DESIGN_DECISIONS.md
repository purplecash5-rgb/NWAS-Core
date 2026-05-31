# Design Decisions

## 2026-05-31 - Publish framework only, keep data layers private

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
