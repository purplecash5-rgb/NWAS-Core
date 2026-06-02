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

## Core Concepts

- Research Profile Contract: defines safe, auditable retrieval/research modes
  using explicit source, iteration, export, and audit constraints.

## Current Status

NWAS-Core is an early public OSS framework scaffold.

It is suitable for reviewing the architecture and governance direction,
including public schemas, validation ideas, and synthetic examples.

It is not a production knowledge package. It includes no third-party corpus,
private profile layer, deployable data store, or domain-specific knowledge
database.
