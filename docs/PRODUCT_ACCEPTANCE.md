# DOGE TCG — Product Acceptance Gates

## Playable alpha
- Two players can complete matches using legal 30-card decks (for 18-card subset use deliberately labeled alpha deck exceptions).
- Core and Signal victory are both achievable; simultaneous outcomes are deterministic.
- Three-lane front/rear positions, Guard, Quickdraw, Phase, Salvage, Scry, Pack, Pierce have unambiguous executable semantics, or are explicitly deferred.
- Invalid moves are rejected with no state mutation. Replays match exact state hashes.
- Keyboard/touch accessibility, legible card text, turn timer, undo only where rules permit, full turn history.

## Ranked beta
- Six playable factions and 111 executable card definitions with complete effect grammar.
- All 144 digital QA scenarios translated to executable tests or documented manual protocols; 71 physical scenarios tracked separately.
- Mirrored-seed bot simulations and human playtests with recorded win rates, duration, disconnects, deck diversity, first-player advantage, Signal/Core win distribution.
- No P0 or P1 known issues; independent review of deterministic engine and auth.

## Collectible beta
- Wallet ownership displayed with block height and confidence/finality policy.
- Owned vs free-play cards clearly distinguished. No cosmetic rarity power advantage.
- 111 art recipes map one-to-one to definitions; no false claims that prompts alone reproduce identical pixels.
- Pack redemption independent verifier and security review completed before paid distribution.

## Physical future gate
- Game can be played with physical counters, no untrackable automatic effects, printable rules and board.
- Prototype tabletop matches measured before any print manufacturing commitment.
- No scan-to-NFT entitlement without single-use tamper-resistant claim design and explicit split-ownership policy.
