# Optional Model Layer

NWAS-Core uses the term optional model layer for language-understanding,
suitability-judging, and drafting components.

The optional model layer is swappable. It should receive evidence packets and
governance constraints, then return structured draft metadata for validation.

It must not be treated as the source of authority. A validator should reject
outputs that lack evidence support, overstate certainty, or ignore review flags.
