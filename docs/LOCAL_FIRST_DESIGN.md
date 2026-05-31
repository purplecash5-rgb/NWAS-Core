# Local-First Design

NWAS-Core favors local ownership of data and review decisions.

Public framework code should be able to run without hosted services, private
cloud indexes, or bundled corpora. Operators may add their own storage and model
runtimes, but private data layers should remain separate from this repository.
