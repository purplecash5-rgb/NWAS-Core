# Architecture

NWAS-Core describes a local-first, evidence-governed knowledge framework.

The public architecture is organized around five replaceable layers:

1. Corpus adapter: reads a lawful corpus supplied by the operator.
2. Retrieval interface: returns candidate source records and citation pointers.
3. Evidence packet builder: packages candidate evidence with provenance.
4. Optional model layer: judges suitability and drafts language from evidence.
5. Governance validator: checks answer mode, citations, flags, and review state.

The optional model layer is not an authority source. Authority comes from the
operator's lawful sources, source ranking rules, and governance checks.
