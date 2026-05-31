# NWAS-Core

NWAS-Core is the public framework layer for NWAS. It documents the architecture,
governance model, schemas, validators, and synthetic examples needed to build a
local-first evidence-governed knowledge system.

This repository does not include private knowledge packages, third-party
corpora, model outputs derived from private data, or deployable data stores.
Bring your own lawful corpus and keep private data in a separate layer.

## Repository Layout

- `docs/` - public architecture, governance, policy, and progress notes.
- `schemas/` - JSON schemas for portable public framework contracts.
- `examples/toy_corpus/` - tiny synthetic sources for tests and demos.
- `examples/demo_outputs/` - synthetic governed-answer examples.
- `tests/` - lightweight validation and safety tests.

## Current Status

This is an early public scaffold. Interfaces are intentionally small and
implementation-neutral so downstream projects can adapt them without inheriting
private NWAS data or assumptions.
