# Existing pack protocol integration checklist

**Existing infrastructure is reported, not verified here.** This repo must not create a parallel pack protocol. Inspect existing standard and indexer first.

Record: canonical payloads, supply/odds commitments, entropy source and bias proof, random outcome reproducibility, pack state machine, transaction ordering, signature domain separation, confirmation threshold, chain reorg rollback, duplicate claim behavior, transfer-vs-rip concurrency, output ownership, failure recovery, DMP listing integration, and indexer consistency.

Document exactly which properties are consensus-enforced on Dogecoin versus interpreted by the metaprotocol/indexer or trusted service. Independent verification is a requirement; claims of trustlessness need evidence.
