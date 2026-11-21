# Build plan and approval gates

## Gate 0 — Discover actual existing stack
Inventory repositories, endpoints, commits, package scripts, deployment boundaries, schemas, and test coverage for: doginals.lol site/route; pack-ripping metaprotocol and randomness; indexer; wallet; marketplace; drok.lol art tools. Read-only only. Fill `architecture/INTEGRATION_MATRIX.md` with evidence. Private repos are **UNKNOWN** until made accessible.

## Gate 1 — Freeze playable rules
Resolve all open decisions in `decisions/DECISION_REGISTER.csv`. Specify 3 lanes, 30 cards, Core 20, Signal 8 only if validated by playtests. Define turn/phase order, priority windows, costs, targeting, simultaneous triggers, deterministic ordering, hidden info, mulligan, fatigue, tie conditions, deck limits, effect grammar, stack/loop caps, and tabletop handling. Obtain explicit owner sign-off.

## Gate 2 — Playable vertical slice
18 representative **gameplay** definitions across mechanics, not merely art prompts. Deterministic pure reducer, action validator, replay verifier, state hashes, CLI/hotseat match, automated unit/property/fuzz tests. Include full match replay fixtures and at least one human tabletop dry run.

## Gate 3 — Online game
Server authoritative turns; wallet auth via existing stack; matchmaking, reconnect, timers, spectators, anti-cheat, state privacy, deck builder and collection UI. No live chain dependency during active match.

## Gate 4 — Genesis 111
Create actual card data in a separate gameplay manifest, validate balance and all 6x6 faction matchups. Art recipes derive from locked abilities, faction, pose, and role. Keep editions cosmetic.

## Gate 5 — Integrate on-chain
Adapt existing pack-ripping, indexing, wallet and trading. Validate supply accounting, random outcome evidence, replay/double-claim resistance, transfer during redemption, reorg recovery, ownership snapshots, listing settlement and reconciliation. Do not invent a second protocol.

## Gate 6 — Art production
Connect existing drok.lol generation API after source verification. Generate lazily per card, store prompt/version/model/seed/reference/content hash; validate transparency and no embedded card UI. Separate printable card frame and data typography.

## Gate 7 — Launch and later tabletop
Complete security review, legal/commercial review for paid randomized packs, accessibility, performance, load and incident drills. Physical production remains contingent on online success and tabletop parity.

## Hard release blocks
Unresolved critical rules ambiguity; replay divergence; client-authoritative match outcome; unverified pack randomness; inconsistent indexer ownership; missing reorg handling; unsafe wallet signing; unreviewed paid pack compliance; production chain writes without approval.
