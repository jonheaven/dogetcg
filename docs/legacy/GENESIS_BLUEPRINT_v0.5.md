# DOGE TCG — Genesis 111
## Product, rules, collection, and Dogecoin protocol blueprint v0.5 — QA and physical expansion specification
**Date:** 2026-11-21  
**Status:** Proposed design, not a finalized or audited protocol.

## 1. North star
**DOGE TCG** is a free-to-learn competitive card battler where collectors own scarce Doginal editions, sealed packs, and card art, while every player can access a fair competitive ruleset. Ownership, edition provenance, pack commitments, and selected match proofs are anchored to Dogecoin L1. Fast turn-by-turn play happens off-chain with verifiable deterministic replays. This distinction is essential: Dogecoin L1 cannot economically or responsively execute each interaction as a smart-contract TCG.

**Positioning:** Dark, detailed monochrome Doge warriors, Dogecoin-native lore, high skill ceiling, no meme-coin casino mechanics, no prerequisite NFT purchase. **Art is desirable even without the game; gameplay is enjoyable even without NFTs.**

**Non-negotiables:** No pay-to-win stats; no secretly mutable rarity; no unauthorized IP/art appropriation; no paid competitive advantage; free starter decks; accessible readable card text; real deterministic game tests; no promises of investment returns.

## 2. Lessons from leading TCGs and NFT collections
| Reference | Proven pattern | Adopt | Avoid |
|---|---|---|---|
| Pokémon TCG | 60-card decks, prize race, approachable combat | Visible progress toward victory; mascot-quality characters | Exact prize/energy mechanics or copied iconography |
| Magic: The Gathering | Deep deck construction, priority/stack, rotating formats | Counterplay, precise rules and evergreen format | Excessive timing complexity at launch |
| Disney Lorcana | Alternative scoring race; cards as resources | A secondary scoring objective | Copying lore/ink structure directly |
| Parallel | Bank cards for flexible energy | Reduce resource screw | Duplicate its bank economy |
| Gods Unchained | Free gameplay with tradable NFT editions | Separate digital play access from ownership | Token speculation as substitute for retention |
| CryptoPunks | Distinct silhouettes, limited original collection, provenance | Recognizable PFP identity, permanent numbered genesis | Mechanically powerful rarity |
| BAYC | Character identity and social belonging | Community identity and collector display | Exclusivity as the only utility |
| Art Blocks | On-chain generative provenance | Reproducible metadata and media manifests | Unverifiable trait generation |
| Parallel / other web3 TCGs | NFT editions alongside a playable client | Card art plus real utility | Wallet friction before first game |

Sources and research entry points: Pokémon rulebook https://assets.pokemon.com/assets/cms2/pdf/trading-card-game/rulebook/pal_rulebook_en.pdf ; Magic rules https://magic.wizards.com/en/rules ; Parallel manual https://parallel.life/game-manual ; Gods Unchained FAQ https://store.epicgames.com/p/gods-unchained-faq-59d51d . Further primary-source verification is required for market sizes and current NFT project activity.

## 3. World and lore: THE LONG CHAIN
After the Great Silence, the Chain continues to produce blocks, but its frontier is fragmented into six domains. Six rival orders compete to secure the **Finality Gates**, ancient checkpoints whose signatures determine which history survives. No one owns the Chain. Every faction claims to defend it. Doge is the common ancestor, not a proprietary collection. The visual universe combines ronin, western outlaws, cybernetic sentinels, cryptographic mystics, wasteland salvagers, and frontier mercenaries. Humor lives in small details and card names, never in clownish character designs.

### Six archetypes / factions
| Faction | Fantasy | Playstyle | Weakness | Signature mechanic |
|---|---|---|---|---|
| **Ironclad** | armored validators, shield-bearers | control, fortification | slow pressure | **Guard**: protect a lane |
| **Outriders** | gunslingers, raiders, bounty hunters | tempo, precision removal | fragile bodies | **Quickdraw**: act immediately on deployment, with restrictions |
| **Ghostline** | stealth scouts, cypherpunks, infiltrators | misdirection, mobility | poor sustained defense | **Phase**: relocate between lanes |
| **Ashbound** | burn wardens, wreckers, scavengers | attrition, discard recursion | self-inflicted costs | **Salvage**: recover from discard with limits |
| **Runekeepers** | arcane archivists, chain scholars | combo, card selection | setup-dependent | **Scry**: inspect/reorder deck top |
| **Wildpack** | wandering shibes, beasts, insurgents | swarm, coordinated attacks | board wipes | **Pack**: bonuses from allied presence |

**Faction identity:** Players choose one faction plus up to six neutral cards. Dual-faction support is a later format, not launch. Each faction needs at least one credible aggro, midrange, and control path over time.

## 4. Genesis 111 — collectible card identities
**Recommended 111 card definitions:** 60 Units (10/faction), 24 Tactics (4/faction), 12 Relics (2/faction), 9 Neutral Units, 6 Neutral Tactics. Each definition is a distinct card design, not a single minted NFT. Printed supply is a separate edition system.

### Definition rarity and mint rarity must be distinct
**Gameplay rarity** (Common, Uncommon, Rare, Legendary) denotes complexity and deckbuilding limits, **not power**. **Edition rarity** denotes scarcity and art finish (Standard, Foil, Obsidian, Genesis Signature). A rare edition of a card has *identical game rules* to the standard edition. Never let NFT metadata change competitive attack, health, or costs.

### Sample named characters
**Ironclad:** The Last Validator; Bastion-86; Chainwarden; Iron Muzzle; Cold Storage.  
**Outriders:** Two-Gun Shibe; Dust Marshal; Zero-Conf; Blackpowder; The Longshot.  
**Ghostline:** Ghost Runner; Silent Relay; Nullshade; Shadow UTXO; The Watcher.  
**Ashbound:** Burn Warden; Ash Collector; Dead Output; Cinder Fang; The Reclaimer.  
**Runekeepers:** The Archivist; Keeper of 420; Hexscribe; The Oracle; Witness Zero.  
**Wildpack:** Alpha of the Commons; Feral 69; Bonebreaker; Packrunner; Last Howl.

Names referencing protocol concepts should be understandable as flavor without requiring crypto knowledge. Use actual Dogecoin historical references only where accurate, and do not imply endorsement from identifiable people.

## 5. Gameplay — proposed playable alpha rules
### Match format
- 1v1, best-of-one, **30-card decks**, exactly one faction, maximum two copies per named card; Legendary definitions limited to one. No more than six neutral cards.
- Each player starts at **20 Core Integrity** and **0 Signal**. First to **8 Signal** wins at the next state-based check; reducing enemy Core Integrity to zero also wins.
- Battlefield has **three lanes**. Each lane supports up to **two allied Units**. Only one Unit in each lane can be in the Front position; the other is Rear. A lane with an enemy Front must be cleared before attacking enemy Core through that lane.
- Each turn: ready exhausted units, refill **Charge**, draw one card, main phase, combat, end phase. Going first: skip first-turn draw and cannot attack on turn one.
- **Charge** automatically increases by one maximum per turn up to 8, then refills each turn. This avoids mana screw and card banking overhead. No separate resource cards.
- Units have **Cost / Attack / Health / Speed**, a faction and one or fewer evergreen keywords initially. Damage persists until healed; a unit with zero Health is discarded.
- Deploying a Unit normally exhausts it for the current turn. During combat, each ready Unit can attack once. Defenders deal simultaneous counter-damage when fighting units. A unit may attack the opposing Core only if its lane has no enemy Front Unit.
- A ready Unit may **Secure** its lane instead of attacking: if there is no enemy Front Unit in that lane, gain **1 Signal**, maximum 2 Signal from Secure per turn. Securing exhausts the Unit. This creates a positional race distinct from direct damage.
- **Tactics** are one-shot spells played during main phase unless explicitly marked **Reaction**. Reactions use a single alternating response window, maximum one response from each player, then resolve last-in-first-out. No arbitrary stack loops in alpha.
- **Relics** occupy one of two global Relic slots and provide persistent effects. Uniques are one per board.
- Start with 4 cards. Each player may mulligan once by shuffling any number of chosen cards into the deck and drawing that many. Starting player chosen by verifiable seeded randomness.
- Deck-out: a player required to draw from an empty deck loses. Simultaneous victory triggers: active player loses, preventing advantageous ambiguous ties; revisit after testing.
- No paid items, editions, serial numbers, or historical ownership alter these rules.

### Core keyword glossary
**Guard**: enemies in this lane must target this unit before other allied units here. **Quickdraw**: may attack enemy Units on the turn deployed, but not Core or Secure. **Phase**: once per turn, move this Unit to an adjacent lane if there is room. **Salvage N**: when played, return a friendly Unit of cost N or less from discard to hand, once per card play. **Scry N**: inspect top N cards, reorder them. **Pack**: specified effect if another allied Unit occupies a lane. **Pierce**: excess combat damage may hit Core only when explicitly granted by card text. Define triggers and exact ordering in machine-readable rules before minting.

### Design guardrails and balance targets
Target match length 8–15 minutes, meaningful decisions by turn 2, no reliable turn-3 wins, and at least 40% of games decided by the Signal route during alpha (hypothesis, not measured). Watch first-player win rate, faction matchup spread, dead-hand frequency, average actions/turn, and time-to-first-fun. Balance by changing a **versioned ruleset**, never silently altering historical metadata; publish a changelog and allow legacy replays.

## 6. Five fully specified prototype cards
| Card | Faction/type | Cost | A/H | Text |
|---|---|---:|---|---|
| The Last Validator | Ironclad Unit | 5 | 3/7 | Guard. When deployed, another friendly Unit in this lane gains +0/+2 until end of turn. |
| Two-Gun Shibe | Outriders Unit | 3 | 3/2 | Quickdraw. If this defeats an enemy Unit on deployment turn, gain 1 Signal (once). |
| Ghost Runner | Ghostline Unit | 2 | 2/2 | Phase. After moving, this gains +1 Attack until end of turn. |
| Burn Warden | Ashbound Unit | 4 | 3/4 | When a friendly Unit is discarded from play, deal 1 damage to the opposing Core (once per turn). |
| The Archivist | Runekeepers Unit | 3 | 1/4 | On deploy, Scry 3, then draw a card. |

These are **test values**, not balanced final cards. Need initial 111-card CSV/JSON design with tests before publishing immutable game definitions.

## 7. Pack design and collectible economy
### Pack contents
A proposed **Genesis Pack** contains 5 card editions: 3 standard slots, 1 uncommon-or-better slot, 1 foil/variant slot. The fifth slot's variant may be Standard in budget packs if the odds are explicitly disclosed; never imply guaranteed rare finishes. All 111 card definitions can also be earned/borrowed as nontransferable digital gameplay licenses in the free client. Physical-style rarity and edition scarcity should not gate deck construction.

### Why hold sealed packs?
1. **Provable untouched state:** a sealed pack is a distinct collectible with its own serial, art, and mint timestamp.
2. **Known fixed supply:** only a bounded number of Genesis packs ever issued, with transparent allocation and unsold treasury handling.
3. **Independent sealed market:** unopened packs can be traded as their own Doginal objects.
4. **Reveal ceremony:** opening transforms a sealed asset into a recorded redeemed state plus five newly owned card editions.
5. **No arbitrary re-rolls:** each commitment redeems exactly once; duplicates are legitimate outcomes.

**Critical:** Scarcity and uncertainty may attract collectors, but don't design artificial pressure to gamble, promise appreciation, or sell opaque odds. Publish exact supply, probabilities, pack guarantees, fees, and redemption behavior before sale. Consider legal review for paid randomized packs and secondary markets, especially minors and cross-border sales. No cash-out gaming rewards or wagering.

### Proposed edition allocation (not launch promise)
Standard 75%, Foil 20%, Obsidian 4.5%, Signature 0.5% **across variant slots only**, with explicit per-definition allocation and auditability. A Signature edition is cosmetic and has no extra power. Run economic simulations before committing these figures.

## 8. Pack cryptography and Dogecoin constraints
A naïve server RNG is not enough. A simple reveal hash alone does not prevent a seller from cherry-picking outcomes if the seller knows the seed and can choose which packs to distribute.

**Recommended design path:**
1. Inscribe immutable `set_manifest` with card definitions, art references, edition caps, odds, random selection algorithm, and `ruleset_hash`.
2. Inscribe or commit to a **batch Merkle root** of individually serialized packs and precommitted encrypted or hidden contents; use independently contributed entropy **after pack allocation is fixed** to prevent issuer grinding. Document exact entropy trust assumptions and fallback paths.
3. Each pack has a unique ID, allocation record, and state machine: `MINTED -> SEALED -> REDEEM_REQUESTED -> REDEEMED`. Ownership transfers while SEALED do not open it.
4. Pack owner authorizes redemption with a wallet signature referencing pack outpoint/ID, nonce, and destination. A verifier checks current canonical owner and replay protection.
5. The minting/redeeming coordinator must atomically ensure the pack is marked redeemed and five output cards are issued; on Dogecoin L1 this may require a **protocol indexer with explicit reorg and partial-failure handling**, because arbitrary smart-contract atomicity is unavailable.
6. Publish Merkle proofs, reveal transcripts, randomness proof, output inscription IDs, and reconciliation reports. Anyone should be able to reconstruct contents from public records after reveal.
7. If noncustodial atomic redemption cannot be achieved safely, launch a clearly disclosed coordinator-assisted MVP rather than claiming trustlessness.

**Important unresolved feasibility question:** A Doginal inscription does not automatically behave like a programmable smart contract. Pack redemption, binding contents to outputs, delegated art references, and market transfers need a **fully specified, independently implemented metaprotocol indexer**, wallet-signing conventions, and tests. Recursive rendering is a content-loading technique, not execution consensus.

## 9. On-chain architecture
**Layer A — immutable content:** art originals (transparent PNG/WebP or optimized SVG where suitable), reusable visual elements, edition frames, card text/definitions, hashes, set manifests. Inscribe immutable content-addressed assets and link them with explicit versioned IDs.

**Layer B — Doginal ownership:** pack inscription IDs, edition inscription IDs, serials, ownership via UTXO tracking. Define reorg behavior, transfer indexing, unspendable outputs, double-spends, and pending-confirmation states.

**Layer C — metaprotocol events:** `SET_REGISTER`, `PACK_MINT`, `PACK_REDEEM`, `CARD_MINT`, `CARD_TRANSFER` (where necessary), `SEASON_COMMIT`, `MATCH_RESULT_ROOT`. Every event needs a version, canonical ordering rule, deterministic parser, signature verification, and validation rules. Avoid redundant events if UTXO transfers already prove ownership.

**Layer D — game engine:** TypeScript or Rust deterministic state transition engine, signed player inputs, match seed commitments, event log, replay validator, ruleset hashes, automated fuzz/property tests. Host live games on a low-latency server. Periodically commit batches of results or replay roots to Dogecoin, rather than every turn.

**Layer E — client:** browser-first responsive board, guest/free play, deckbuilder, wallet connect, collection gallery, marketplace, pack opening, tournaments, spectator/replay mode. The UI should work before any wallet is connected.

### Minimal conceptual metadata
```json
{
  "protocol": "doge-tcg",
  "version": "0.1",
  "kind": "card-edition",
  "set": "genesis-111",
  "definition_id": "G111-001",
  "edition": "obsidian",
  "serial": 17,
  "art_inscription": "<inscription-id>",
  "definition_inscription": "<inscription-id>",
  "ruleset_hash": "<sha256>",
  "metadata_hash": "<sha256>"
}
```
This is a **proposed schema**, not an existing published standard. Inscription IDs and ownership proof formats must be validated against the actual Doginals tooling and your metaprotocol specification.

### Wallet and marketplace integrations
Reuse your existing Dogecoin tooling where it passes audit: **kabosu** for indexing, **dogestash** for wallet operations, **DMP** for listings and settlement, and **doginals.lol** for discovery. Do not assume they currently implement every feature above. Make ownership queryable from multiple independent indexers; integrate listings and purchases only after PSBT flows and replay protection are verified.

## 10. Art bible — collectible before card frame
- Black/white high-contrast, etched metal and distressed cloth, gritty illustration, detailed Shiba facial expression; no childish chibi proportions.
- Individual **transparent-background character masters** at consistent canvas sizes and safe margins. Keep weapon tips and cloaks inside the cutout boundary.
- Maintain consistent head-to-body proportions and eye/muzzle anatomy; diversify silhouettes and poses, not merely equipment recolors.
- Faction-specific silhouettes: shield/hammer, pistols/dusters, visor/blades, lantern/chains, scrolls/arcana, claws/bone armor.
- Generate characters without lettering, card UI, numbers, watermarks, or logos. Apply card border, title, stats, edition finish, and faction sigils programmatically as separate layers.
- Deliverables per card: lossless RGBA master, compressed web asset, alpha-mask validation, thumbnail, portrait crop, image hash, metadata manifest, and licensed provenance record.
- Verify actual transparency in the output alpha channel; a checkerboard-looking RGB background is **not** transparency.
- The card must remain recognizable at 64px; test facial legibility and distinct silhouette.

### Six hero briefs
1. **The Last Validator** — giant shield, block-etched warhammer, cathedral armor, unshakable gaze.
2. **Two-Gun Shibe** — tattered western hood, twin heavy revolvers, silver gauntlets, confident smirk.
3. **Ghost Runner** — narrow visor, hood, dual blades, low mobile posture, stealth utility gear.
4. **Burn Warden** — ash-stained cloak, hanging iron brazier, chains and ember scars.
5. **The Archivist** — rune-marked plate, fractured data-scrolls, relic staff, watchful expression.
6. **Alpha of the Commons** — feral warleader, wolf-fur mantle, bone armor, massive spear.

## 11. Product experience and viral loops
**First 60 seconds:** landing -> Play Now -> choose faction starter -> tutorial battle (no wallet) -> win/lose -> view deck -> optional wallet connection. No token purchase required.

**Collector loop:** browse art -> inspect edition/serial -> open or trade pack -> show collection -> set favorite Doge as PFP -> showcase in battle. Every character has a standalone portrait export with clear ownership display; card frames are optional.

**Competitive loop:** free queue -> daily quests (cosmetic only) -> ranked ladder -> public decklists -> replay sharing -> faction leaderboard -> seasonal tournaments. Reward skill with titles, cosmetics, and prestige, not speculative yield.

**Community loop:** deck codes, spectatable tournaments, creator-led faction battles, public rarity audit, on-chain mint explorer, Dogecoin culture cameos subject to permissions. Build for streaming and X sharing with one-click highlight clips.

## 12. Formats and longevity
**Genesis Standard:** genesis set only, fixed rules version during season. **Eternal:** all released cards with a transparent ban/restriction list. **Draft:** randomized temporary pool with equal access; free or flat-fee non-wagered events. **Sealed:** digital event decks from packs (do not require burning owned assets). **Pauper:** commons-only definitions. **Showcase:** collectible edition-only visual battles with no competitive modifier.

**Set expansion policy:** Add cards only when they increase strategic diversity; do not obsolete the entire previous set. Keep old art permanently available. Every new expansion ships with matchup simulations, power-budget reports, and a public rules changelog.

## 13. Metrics, milestones, and stop/go gates
**Prototype (weeks 1–4):** deterministic engine, 18 starter cards (3/faction), three-lane board, bot opponent, no blockchain. Gate: 1000 automated matches without invalid state; players understand scoring after one tutorial.

**Alpha (weeks 5–10):** 54 tested cards, multiplayer, replay engine, ranked prototype, art direction locked. Gate: 100 human matches, clear top frustrations, no dominant faction above 60% win rate in adequately sampled matchups.

**Beta (weeks 11–18):** full 111 definitions, public deckbuilder, wallet read-only ownership, verified indexer, pack reveal testnet/sandbox simulator. Gate: independent verifier reproduces all outcomes and match replays.

**Genesis release (only after audit):** immutable manifest, capped editions, actual on-chain pack redemption, marketplace, transparency dashboard, ranked season. Gate: security audit, legal review, incident response and recovery runbooks, documented fees and failure states.

These are planning estimates, not a delivery guarantee. Development effort may be substantially longer for a small team.

### Core KPIs
D1/D7/D30 retention, tutorial completion, games/player/week, median match duration, first-player advantage, faction matchup spread, pack reveal failure rate, redemption cost, independently verified ownership correctness, active marketplace depth, organic deck-share rate, and share of players who play without owning NFTs.

## 14. Key risks and decisions
1. **Blockchain performance:** Never promise every turn is settled on Dogecoin. Own assets on-chain, anchor proofs; gameplay off-chain.
2. **Pack fairness:** Publisher manipulation and issuance after reveal must be impossible or clearly disclosed as trusted.
3. **Spec compatibility:** Verify existing metaprotocol, recursive and delegate support before hard-coding schemas.
4. **Regulation:** Paid random packs and resale can raise consumer, gambling, and youth-protection issues; get jurisdictional advice.
5. **Supply economics:** 111 *definitions* is not 111 playable NFT copies. Pick pack count and edition supply only after modeling.
6. **Card balance:** Scarcity must not create stronger stats; tournament access should be free.
7. **IP and trust:** Original Doge-themed artwork, careful handling of Dogecoin trademarks and recognizable real-world likenesses.
8. **Security:** Wallet signatures must be domain-separated and never ask players to sign opaque transfers; simulate malicious marketplace and indexer conditions.
9. **Operational cost:** Budget inscription fees, asset size, server costs, and customer support before pack pricing.
10. **Launch strategy:** Gameplay-first vertical slice before selling packs. Players, not mint revenue, validate the project.

## 15. Decisions I recommend locking now
- Name: **DOGE TCG**. Set: **Genesis 111**. World: **The Long Chain**.
- Six factions, 111 unique definitions, 30-card decks, three-lane combat, dual victory paths (Core or Signal).
- No NFT required for ranked play; owned editions provide display, provenance, and trading rights.
- Transparent character cutouts first, cards composed from separate reusable layers.
- Sealed packs are distinct transferable Doginals; revealing must be deterministic and publicly auditable.
- Launch game engine before pack sale. DOGE is the payment currency; **do not issue a new game token**.

## 16. Immediate work order
1. Build a JSON schema and deterministic rules engine for the five sample cards and a 12-card microdeck.
2. Playtest 30–50 games; tune Signal victory and lane movement.
3. Finalize six faction art references and generate one iconic hero per faction.
4. Expand to 18 starter cards, then 54, then all 111.
5. Write and independently test the pack commitment/redemption protocol.
6. Implement collection viewer, wallet ownership, and trade links.
7. Open a free public alpha, recruit competitive TCG players, and fix gameplay before minting.

**Creative thesis:** Make players say *“this is a great card game”* before they say *“these are NFTs.”* Make collectors say *“I would wear that character as my avatar”* before they learn its stats.


## 17. Lazy art generation — reproducible 111-card production pipeline (v0.2 addition)

**Goal:** Define art for all 111 Genesis cards today without generating any final images until needed. The accompanying `DOGE_TCG_ART_MANIFEST.json` is the **canonical prompt catalog**: exactly 111 individually addressed art recipes, each containing a complete runnable prompt, negative prompt, deterministic seed hint, references, canvas specification, approval status, and future output/hash fields. `generate_doge_art.py` is the batch runner with a provider-adapter interface.

### Identity vs recipe vs immutable image
- **Card identity:** `card_id` (`DTCG-G111-001` … `DTCG-G111-111`), `card_name`, `faction`, `card_type`. These never change because of a new image.
- **Art recipe:** `art_recipe_version`, `prompt`, `negative_prompt`, `reference_asset_ids`, `seed_hint`, `canvas`, `model_provider`, `model_id`, `model_version`, `model_parameters`. Prompts can be revised *before* mint, with version history. Any post-mint visual change creates a separately identified art revision, never a stealth overwrite.
- **Approved art:** lossless RGBA master, SHA-256 digest, final media URI/inscription ID, approval status, and provenance. A hash binds the exact pixels/bytes. A seed/prompt does **not** guarantee pixel-perfect regeneration after model, sampler, or infrastructure changes.
- **Gameplay:** rules IDs and stats live in a *different* manifest; art cannot modify cost, attack, health, abilities, or legality.

### Files
| File | Purpose |
|---|---|
| `DOGE_TCG_ART_MANIFEST.json` | One complete prompt + metadata record per card, ready for lazy generation |
| `generate_doge_art.py` | Generate by ID, faction, or all; never silently overwrite existing PNGs |
| `art/references/samurai_doge_reference_v1.png` | User-provided samurai style reference; freeze and hash original bytes |
| `art/references/hooded_gunslinger_reference_v1.png` | User-provided gunslinger style reference; freeze and hash original bytes |
| `art/generated/DTCG-G111-001.png` | Example output naming convention; outputs are not yet generated |
| `art/generated/DTCG-G111-001.generation.json` | Generation receipt, prompt digest, asset digest, review state |

**Important:** The 111 recipes are production-ready *draft briefs*, not a claim that all 111 card rules or their final illustrations have been approved. The 60 faction Units, 24 faction Tactics, 12 faction Relics, 9 Neutral Units and 6 Neutral Tactics have all been individually named and assigned prompts. Non-unit cards use isolated action or artifact art rather than forcing a full-body portrait. Review all names for consistency with future finalized card mechanics.

### Prompt structure
Each card has a full self-contained prompt combining: (1) fixed global monochrome engraving style, (2) faction silhouette/material language, (3) unique subject and signature equipment/action, (4) pose/composition, (5) alpha-background requirements and negative constraints. Store the exact final prompt in JSON instead of constructing it dynamically at mint time. The shared style text is additionally preserved as `style_master` for editorial review.

### Generation examples
```powershell
python -m pip install Pillow
python generate_doge_art.py --list
python generate_doge_art.py --card DTCG-G111-001 --dry-run
python generate_doge_art.py --faction Ghostline --dry-run
python generate_doge_art.py --all --dry-run
# After implementing your provider adapter:
python generate_doge_art.py --card DTCG-G111-001 --provider-module my_image_adapter
python generate_doge_art.py --faction Ironclad --provider-module my_image_adapter
python generate_doge_art.py --all --provider-module my_image_adapter
```
The runner is **provider-neutral**, not a functioning image API client until `my_image_adapter.py` implements `generate(prompt, negative_prompt, seed, width, height, reference_paths) -> PNG bytes` using the chosen provider. It does not assume that a ChatGPT subscription grants API access. An adapter must persist actual model/version, sampling parameters, API job ID, and any reference-image digests in a durable generation log. Some providers cannot honor seeds, reference inputs, or native alpha; adapters must declare unsupported controls rather than falsely promise reproducibility. Generate transparent output natively when possible, otherwise perform explicit background removal and validate the resulting RGBA file.

### Pre-generation preparation and art QA
1. Place the **original two user-provided reference images** under the exact reference paths above, and commit their SHA-256 hashes in an asset-lock manifest. Preserve rights/license documentation for all future reference images.
2. Pick and freeze one provider/model revision and record API request parameters; test 3–6 faction heroes first, then approve a visual style lock. Different model families may interpret the same prompt very differently.
3. Generate **only missing assets** on demand. Keep draft renders separate from `approved/`; don't overwrite approved art even with `--force` (use `--force` only for expendable drafts).
4. Validate dimensions, actual transparent alpha (not a painted checkerboard), no cut-off weapons, recognizable Doge anatomy, no unwanted lettering, no malformed paws, and distinguishable silhouette at 64 px. The included runner checks only basic PNG/alpha invariants; human visual QA is mandatory.
5. Record reviewer, approval timestamp, source prompt hash, reference hashes, model fingerprint, output hash, and final inscription/delegate references in an append-only approval record. Generate thumbnails and PFP crops as **derivatives** with separate hashes.
6. Compose final trading cards with programmatic layers: background, faction styling, character cutout, frame, title, stat icons, rules text, edition treatment. **Never bake mutable card stats or UI into character artwork.**
7. For recursive Doginals, inscribe or reference immutable approved media and metadata by verified identifiers, and freeze the edition manifest. Treat delegate/recursive support as a protocol-compatibility requirement to verify against the actual indexer and metaprotocol implementation.

### Regeneration policy
- **Before mint:** revise prompt with new `art_recipe_version`, regenerate drafts, visually approve, and lock one final asset digest.
- **After mint:** do not change the original inscription's art pointer or misrepresent a newly generated image as the original. Issue an explicit revision/alternate-art edition with a distinct immutable media reference if desired.
- **Disaster recovery:** first restore the exact approved original from content-addressed storage or inscription bytes and verify SHA-256; use AI regeneration only as a *new approximate rendition*, not as a substitute for the original asset.
- **Bulk migration:** run the catalog through a newly versioned provider adapter, review differences, and publish new edition references only with transparent provenance.

### Production checkpoint
All 111 prompt records now exist; **zero final character artworks are claimed generated or approved by this manifest**. Freeze the prompt catalog in version control and start by testing the six faction heroes, then iterate the art direction before spending on all 111.

---
## 18. Game-first design freeze and art derivation gate (v0.3)

**Status: PROPOSED, NOT LOCKED.** This section supersedes any implication that the v0.2 card prompts are production-ready. The 111 existing art prompts are *provisional character sketches*, not canonical art instructions. The original source of truth is gameplay and card definition data, not image prompts.

### 18.1 Design hierarchy
`ruleset.json -> factions.json -> cards.json -> visual_briefs.json -> prompt_templates -> rendered_assets -> approved_asset_manifest -> inscription_manifest`.

* `ruleset.json`: turn sequence, timing, targeting, lane mechanics, victory conditions, balance constraints, version/hash.
* `factions.json`: gameplay identity, strengths, weaknesses, faction visual vocabulary, prohibited overlap.
* `cards.json`: one immutable ID per card, type, costs, stats, keywords, ability text **and structured executable effect**, gameplay role, counterplay, deck archetype, lore anchor.
* `visual_briefs.json`: character or scene type, silhouette, equipment, pose, expression, focal point, visual storytelling of mechanic, faction motifs, composition constraints. Never treat art as evidence of game rules.
* `prompt_templates`: stable shared style, card-type composition, negative prompt, reference IDs, output dimensions, alpha requirements, provider parameters.
* `approved_asset_manifest`: sha256, alpha QC, crop QC, model/version, source prompts, reference hashes, human approval, revision history.
* `inscription_manifest`: immutable content hash and inscription ID for each approved asset and edition; no silent replacement.

### 18.2 What is tentatively fixed vs what needs a decision
**Provisional foundation:** 1v1; 30-card mono-faction decks with up to six neutrals; three lanes; Core 20; Signal 8; Charge 1–8; Units/Tactics/Relics; 111 designs distributed 60/24/12/9/6; no pay-to-win rarity; Doge monochrome etched character aesthetic; sealed Doginal packs and independently verifiable redemption.

**Must resolve before freezing the game:**
1. **Turn and interaction:** exact phase order, whether players alternate whole turns, attack ordering, reaction priority, legal responses, combat targets, whether Front/Rear can be swapped, whether Rear can attack, and how Speed affects actions (currently defined as a stat but unused).
2. **Lane and Signal:** whether an empty lane can be secured, whether Rear can Secure, whether simultaneous attacks are permitted, and how Secure works against Rear-only defense. Proposed default: only ready Front Units Secure, and only when the opposing lane has *no Units*, so Signal requires real lane control.
3. **Timing:** deploy triggers, death triggers, once-per-turn resets, status expiration, replacement effects, multiple triggered effects and deterministic ordering.
4. **Resource curve:** 1 Charge on turn 1 increasing to 8, whether unspent Charge expires, first-turn attack restriction, mulligan behavior, minimum viable early turns, hand limit.
5. **Match end:** when state checks occur, what happens if both Core and Signal win, disconnect/reconnect rules, timer/turn cap, deck-out, draws and tournament adjudication.
6. **Deck rules:** precise copy limits by definition rarity; faction lock; neutral count; rules for cosmetics, duplicates, and card ownership verification without restricting free competitive play.
7. **Card balance:** executable effects and complete stats for all 111; no infinite loops; playable 30-card lists for each faction; tested faction matchups.
8. **Pack protocol:** exact supply, odds, trust assumptions, redemption and reorg semantics, sealed-pack owner verification, legal review. Not a dependency for a fun alpha game.

### 18.3 Proposed alpha clarifications for prototype testing (not final rules)
- **Speed:** remove from alpha card stats unless it has a concrete, tested function; keep Cost/Attack/Health only.
- **Turn:** one active player per turn; refresh, increase max Charge by one (cap 8), refill Charge, draw, main, ordered combat, end; unused Charge does not carry over.
- **Deployment:** newly deployed Units are exhausted unless an explicit keyword permits an action. A Front Unit protects its Rear Unit. Only Front attacks or Secures; Rear supports with printed abilities.
- **Lane movement:** only card effects allow movement. Movement must respect the two-unit lane cap and Front/Rear slots.
- **Secure:** ready Front Unit may exhaust to gain 1 Signal only if the opposing lane has no enemy Units; cap two Signal from Secure per turn. Signal gained from card effects is separately specified.
- **Combat:** attacker selects lane and eligible enemy Front, damage is simultaneous; no enemy Units permits Core attack. Each ready Front attacks once per turn. State-based removals occur immediately after damage.
- **Reactions:** explicit one-response-per-player window after each declared tactic or attack; LIFO resolution, with no new response windows opened by reactions in alpha. Formalize priority in engine tests.
- **No intrinsic power by rarity or edition.** Definition rarity controls complexity and deckbuilding restrictions; art finish controls only appearance.

### 18.4 Every card requires a gameplay-to-art brief
Minimum fields:
```json
{
  "card_id": "DTCG-G111-001",
  "definition_version": "prealpha-0.3",
  "name": "The Last Validator",
  "faction": "Ironclad",
  "type": "Unit",
  "cost": 5,
  "attack": 3,
  "health": 7,
  "keywords": ["Guard"],
  "role": "defensive anchor",
  "mechanical_story": "protects allies and absorbs attacks",
  "lore_hook": "an oathbound guardian of the Finality Gate",
  "silhouette": "tower shield and heavy squared hammer",
  "equipment": ["layered plate", "shield", "hammer"],
  "pose": "shield planted, braced against an incoming strike",
  "expression": "calm, unshakable Doge side-eye",
  "art_type": "full-body transparent character master",
  "composition": "face readable at thumbnail size, weapons inside safe margins",
  "reference_style_id": "doge-engraving-v1",
  "art_approval": "pending"
}
```
This is an illustrative brief, **not a final gameplay or art approval**. Tactics and Relics need dedicated scene/object templates, not 111 humanoid portraits: a Tactic should depict a decisive action, and a Relic should have a standalone iconic silhouette.

### 18.5 Art production acceptance tests
1. No art production batch before `ruleset_hash` and a `card_definitions_hash` exist, with human sign-off on every card's role and visual brief.
2. Render six faction anchors, plus one Tactic and one Relic; approve style consistency before generating the remaining set.
3. Automated checks: real RGBA transparency (not a checkerboard), safe margins, no clipping, output dimensions, file integrity, perceptual similarity/near-duplicates, and expected naming.
4. Manual checks: unmistakably Doge/Shiba (not fox/wolf), expressive face at PFP size, faction silhouette, card-specific ability readable through the art, coherent weapon anatomy, no text/logo/watermark, no unintended duplicate character.
5. Preserve the *exact approved bytes* and hash; a later regeneration is a **new art revision**, not the same immutable inscribed image. A seed alone is insufficient for reproducibility.
6. Keep art masters independent of card frames, stats, rarity foils, and localization. Compose those downstream using deterministic templates.

### 18.6 Design-freeze milestones
- **Gate A — Rules:** one executable ruleset, glossary, and deterministic replay tests.
- **Gate B — Playability:** six starter decks, bot-vs-bot simulation, human testing; revise before freeze.
- **Gate C — 111 definitions:** all card costs/stats/effects/roles/archetypes and counters, automated validation and balance review.
- **Gate D — Visual language:** six approved faction anchors, approved Tactic and Relic conventions, reference image licensing/provenance.
- **Gate E — Prompts:** regenerate every prompt **from structured card briefs**, never maintain prompt text as the canonical source.
- **Gate F — Chain:** immutable art, edition, pack, and redemption manifests only after external verification and security review.

**Immediate next deliverable:** a precise alpha rules specification and 18-card paper/digital test deck, then expand to all 111. Do not inscribe or sell speculative final cards until the design is demonstrably playable.


## 19. Independent QA readiness program (v0.4)

**Assessment status: DESIGN REVIEW ONLY. NO IMPLEMENTATION, SIMULATION, SECURITY AUDIT, OR USER PLAYTEST HAS BEEN PERFORMED.** The companion CSV is a test inventory, not evidence of passing tests. The v0.3 gameplay rules contain contradictions and underspecified timing; the project is **NO-GO for immutable inscription, paid packs, and competitive launch** until resolved.

### 19.1 Severity and release gates
- **P0 blocker:** allows inconsistent winners, divergent replays, unauthorized asset mint/transfer, hidden-information disclosure, broken redemption, unbounded effects, or exploitable paid fairness. Zero unresolved P0s to launch.
- **P1 major:** legal play cannot be completed, common board state ambiguous, balance breaks core experience, inaccessible critical controls. Zero unresolved P1s for public ranked beta; documented exceptions only for closed prototype.
- **P2 moderate:** recoverable UI/visual or uncommon edge case. Documented owner and remediation date required.
- **P3 minor:** cosmetic polish, no gameplay or financial impact.
- **Evidence rule:** Every test requires build hash, ruleset hash, RNG seed, action transcript, initial/final state hashes, expected/actual outcomes, and reviewer. `NOT RUN` never means pass.

### 19.2 Immediate spec contradictions and unresolved design blockers
1. **Front-only Secure versus earlier any-ready-Unit Secure:** v0.3 clarifies Front only, but initial rules remain contradictory. State which section is normative.
2. **Enemy Front versus any enemy Unit for Core/Secure:** the original allows Core damage when Front absent; clarification forbids Secure if any enemy Unit. Proposed consistent rule: any enemy Unit blocks both Core and Secure; Front is target priority, not the sole gate.
3. **Quickdraw versus first-player first-turn attack ban:** declare global prohibition higher precedence or explicit exception.
4. **Speed is defined but has no function:** remove from executable alpha schema.
5. **Simultaneous win active player loses:** exploitable and asymmetric; propose draw, subject to tournament policy and tests.
6. **Reaction timing:** exactly one response each, but no formal priority or trigger timing. Must define an action state machine.
7. **Deck limits vs playable lists:** two copies per card and only 15 definitions per faction (10 Units, 4 Tactics, 2 Relics = 16) plus six neutrals; viable 30-card deck exists, but every faction's curve and options require enumeration.
8. **Rarity and deck limits:** rarity label must not quietly constrain cosmetic variants; legendary definition copy limit should be explicit.
9. **Persistent damage and health buffs:** health maximum versus damage markers, expiration, death checks need canonical arithmetic.
10. **No comprehensive machine-readable effect grammar:** natural language cannot be trusted as deterministic executable rules.

### 19.3 Formal engine contract
**Canonical state:** `(ruleset_hash, match_id, turn_index, active_player, phase, priority_holder, rng_state, players[2], board[3], stack, pending_triggers, action_seq, winner)` with stable instance IDs. Each player has deck ordered list, hand, discard, banish, relic slots, Charge/maxCharge, Core, Signal, per-turn counters. Each unit has owner/controller, lane/slot, base stats, damage, modifiers with expiry, exhausted flag, action history, keyword state.

**Action grammar:** `MULLIGAN_SELECT`, `PLAY_UNIT`, `PLAY_TACTIC`, `PLAY_RELIC`, `DECLARE_ATTACK`, `SECURE`, `MOVE`, `ACTIVATE`, `RESPOND`, `PASS_PRIORITY`, `END_PHASE`, `CONCEDE`, `TIMEOUT`. Each carries match ID, actor, sequence, target IDs, expected state hash, and signed/authorized context.

**Single transition function:** `step(state, action) -> {state, events, error}`; validate authorization, phase, costs, targets, capacity, and timing *before mutation*. Invalid actions return unchanged state. No floating-point arithmetic. No client-trusted RNG, timestamps, or legality checks. Apply effects in deterministic event order, run state-based deaths, enqueue triggers, resolve permitted reactions, then perform victory checks at explicitly documented checkpoints. Record all transitions.

**Required invariants:** (I1) exactly one active player; (I2) no negative Charge; (I3) maxCharge <= 8; (I4) each lane <= 2 units/player and <= 1 Front; (I5) no duplicate instance IDs across zones; (I6) each card exists in exactly one zone; (I7) invalid action leaves state hash unchanged; (I8) exhausted unit cannot attack or Secure absent exception; (I9) Secure gain <= 2 per controller turn, effect gain accounted separately; (I10) match result final and idempotent; (I11) no hidden info exposed to unauthorized player; (I12) same initial state and action log produces identical hashes; (I13) NFT edition attributes never affect game legality or effect output; (I14) no trigger can execute indefinitely; (I15) all action counters and timers are bounded.

### 19.4 Reference timing order (PROPOSED; not frozen)
`declare -> validate -> reserve/pay costs -> response priority -> resolve LIFO (bounded) -> damage/effect application -> state-based removals -> collect triggers -> resolve triggers in canonical order (bounded) -> victory check -> next action`. If target becomes illegal, the effect fizzles but costs remain paid **only if declaration was legal at time of payment**. For combat, determine whether attack exhaustion is a declaration cost; choose and document. Priority pass cannot silently open a new response window.

### 19.5 Scenario inventory and coverage
See `DOGE_TCG_QA_TEST_MATRIX.csv` for individually addressable scenarios, including deck legality, setup, turn economy, all lanes, simultaneous combat, two win conditions, reaction timing, every keyword, zone transitions, network failures, Doginals ownership, pack redemption, provenance, and security. These scenarios must be expanded into executable fixtures with concrete preconditions, exact actions, expected event traces, and expected state hashes. **An inventory is not exhaustive proof of all possible card combinations.**

### 19.6 Combinatorial test strategy
- **Exhaustive small states:** enumerate lane occupancy 0/1/2 for both players across three lanes; enumerate Front/Rear placement and readiness; enumerate Charge 0..8, attack availability, and Signal 0/7/8. Prune unreachable states only with a documented proof or a generator that demonstrates reachability.
- **Pairwise and 3-way covering arrays:** keyword x faction x card type x zone x phase x targeting x simultaneous death x response window; prioritize 3-way interactions for Guard/Phase, Quickdraw/reaction, Salvage/death, and Signal/victory.
- **Property-based testing:** generate legal and illegal action sequences; assert all 15 invariants after every transition. Shrink failures to a minimal replay.
- **Differential testing:** independently implemented authoritative engine and replay verifier must produce identical event/state hashes from the same canonical input.
- **Metamorphic testing:** cosmetic edition swap leaves outcome unchanged; equivalent player-seat swap with swapped seed preserves symmetry where expected; serialize/deserialize mid-match preserves continuation; replay after restart identical.
- **Fuzzing:** corrupt payloads, malformed metadata, truncated inscriptions, integer boundaries, recursion depth, unexpected Unicode, invalid signatures, stale state hashes.
- **Monte Carlo bots:** multiple policies (random legal, aggro, control, Signal rush, disruption) and mirrored seeds; measure matchup variance and first-player bias. This detects problems, not proof of balance.
- **Human tests:** first-time comprehension, skill expression, card readability at 64px, average game time, deck variety, decision load, accessibility, and free-to-play retention.

### 19.7 Balance and mathematical guardrails
With 30 cards and up to 2 copies per definition, a single faction with 16 faction definitions has up to 32 faction-card slots before neutrals; a legal deck can exist, but it may have poor diversity. Compute exact per-faction deck construction counts under all rarity constraints, then sample competitive lists. Test first-player advantage with matched decks and mirrored RNG seeds. Track win by Core vs Signal, turn-to-win distributions, Charge wasted, hand starvation, non-games, faction matchups, play/draw difference, and card inclusion rates. Do not declare 40% Signal victories a balance target without measuring whether the mechanic is healthy.

### 19.8 Dogecoin protocol threat model
Adversaries: issuer, compromised coordinator, malicious pack owner, dishonest marketplace, stale indexer, colluding randomness participants, replay attacker, chain reorganizer, and malicious metadata publisher. Assets: DOGE, pack ownership, edition ownership, contents fairness, supply cap, game records, player privacy.

**Required protocol tests:** canonical transaction/inscription ordering; reorg rollback/reapply; double-spend rejection; signature domain separation; nonce replay prevention; owner-at-height validation; concurrent redeem lock; redeem/mint partial failure and recovery; pack transfer racing redemption; coordinator downtime; independent indexer consensus; Merkle proof verification; deterministic randomness and issuer-bias analysis; exact mint caps; delegated art availability; content-hash verification; recursive renderer cycle and resource limits; DMP PSBT settlement correctness.

**Hard constraint:** an on-chain commitment does not magically enforce atomic issuance on Dogecoin. Do not advertise 'trustless packs' until an independent implementation and audit prove the exact guarantee. Publish all trust assumptions and failure recovery.

### 19.9 Release quality gates
**G0 Spec freeze:** all critical decisions resolved, one normative ruleset, no contradictions, 111 card schema validated.
**G1 Engine alpha:** deterministic reference engine, replay verifier, invariant/property suite, exhaustive small-state checks, zero P0.
**G2 Gameplay beta:** six complete competitive starter decks, 111 executable definitions, card-by-card and interaction tests, observed playtest data, documented balance changes, zero P0/P1 for ranked.
**G3 Asset production:** 111 gameplay-to-art briefs, six faction anchors, approved reference licenses, alpha/silhouette/no-text QA, immutable hashes; prompts derived from approved definitions.
**G4 Protocol beta:** two independent indexers, testnet/regtest-style failure harness where feasible, reorg and race tests, pack randomness review, external security audit, no unaccounted supply.
**G5 Commercial launch:** jurisdiction-specific legal review for paid randomized packs and minors, transparent odds/supply/fees, incident response, backups, support procedures, rollback strategy, public disclosure of centralization.

### 19.10 Exit criteria for the next sprint
Do not generate final card art or mint packs yet. First, approve the 25 decisions in `DOGE_TCG_DECISION_REGISTER.csv`; publish a normalized `ruleset.json` with a formal action/effect grammar; implement an authoritative reducer plus independent replay verifier; encode 18 representative cards; convert at least the P0 inventory to executable deterministic tests. Only after gameplay passes should the 111 card definitions and art prompts be frozen.

## 20. Physical TCG expansion feasibility and digital-to-tabletop bridge (v0.5)
**Status: CONDITIONAL GO for designing tabletop compatibility now; NO-GO for commercial printing or physical-to-NFT redemption until dedicated testing, costing, security review, and legal review.** Digital remains the launch product. This chapter is a future option, not a commitment to physical production.

### 20.1 Executive conclusion and design invariants
A tabletop adaptation is plausible because the alpha uses 30-card decks, a three-lane board, integer Charge, two visible victory tracks, and relatively small board capacity. The strongest obstacle is not card manufacture: it is translating hidden deck information, Scry, reaction timing, persistent damage, temporary buffs, recurring triggers, and priority windows into low-friction human procedures. **One canonical card database and rules identity must drive both digital and print.** Do not promise exact rules parity before testing. Prefer tabletop-compatible design now, with any digital-only exceptions explicitly flagged.

Cross-medium invariants: (P1) same card definition ID/name/faction/cost/base stats/effect semantics; (P2) edition/foil/serial/NFT ownership never change gameplay power; (P3) physical cards playable without phone, internet, wallet, NFT, or app; (P4) physical printing cannot be used to counterfeit or duplicate NFT entitlements; (P5) no hidden issuer ability to increase fixed Genesis digital supply; (P6) a QR code is a locator, never a secret; (P7) no ownership transfer occurs merely from photographing a card; (P8) tournament legality independent of digital possession; (P9) public print/errata versioning and historical preservation; (P10) minors and non-crypto customers can play without blockchain onboarding.

### 20.2 Mechanic-by-mechanic tabletop fit
| Existing mechanic | Physical implementation | Risk | Required design action |
|---|---|---|---|
| Three lanes, Front/Rear, two allied Units/lane | Three-lane foldable playmat, two labeled slots per side | Low | Clearly define front priority, empty slot moves, adjacency |
| Core 20 / Signal 8 | Two counters/dials or paper score track | Low | Exact simultaneous victory rule |
| Charge up to 8, auto-refill | 8 reusable counters, turn/max-Charge dial; spent Charge marked | Low-medium | Specify physical refresh procedure and first-turn rules |
| Attack/exhaustion | Rotate cards 90 degrees or use ready markers | Low | Define whether movement exhausts and attack declaration cost |
| Damage persists | Damage tokens placed on Units | Medium | Test visual clutter and 2-unit lane readability |
| Guard/Quickdraw/Phase/Pack | Keyword reminders and standardized icons | Medium | Write compact tabletop timing rules; avoid nested exceptions |
| Scry N | Privately inspect top N, reorder, preserve deck secrecy | Low-medium | Specify whether opponent sees count/order, shuffle conditions |
| Salvage | Public discard retrieval, bounded once-per-play | Medium | Specify trigger order and discard visibility |
| Tactics/Reactions | Single clearly signaled response window; priority token | High | Resolve whether players can respond during each combat declaration; prohibit ambiguous interrupts |
| Temporary buffs | +A/+H counters with end-of-turn removal | High | Prefer minimal duration effects and bounded counters |
| Multiple simultaneous deaths/triggers | Written active-player/nonactive-player deterministic ordering | High | Provide printed trigger ordering examples and judge guide |
| Relics (two global slots) | Two marked Relic zones | Low | Define replacement, uniqueness, and controller changes |
| RNG or shuffling | Physical shuffle, dice only if strictly required | Medium | Avoid effects requiring server RNG or secret global random state |
| Deck-out / mulligan | Standard manual draw/shuffle procedure | Low | Specify what to do if hand/deck counts are disputed |
| Digital replay verification | Optional companion app, never necessary to complete a match | Medium | Printed match record and judge dispute rules |

**Tabletop complexity budget (proposed):** <=2 active persistent modifiers per unit in typical games; <=3 distinct triggered effects per normal combat; <=1 reaction opportunity per player per declared action; no required smartphone lookup during a match; a first-time player can resolve a turn with a two-page quick-start. These are targets to measure, not facts about the current game.

### 20.3 Three distinct physical/digital ownership models
**Model A — Physical-only print (recommended first):** cards are ordinary licensed physical collectibles, freely tradable and playable; no NFT entitlement. QR may open public card details or optional collection tracker. Cheapest, most accessible, least fraud exposure.

**Model B — Physical product with separately redeemable digital collectible (later):** a factory-inserted, tamper-evident concealed one-time claim code (or sealed redemption insert) is issued against a precommitted allocation. Redeeming through an authenticated service records one claim and delivers a defined NFT edition, subject to the issuer/coordinator trust model. Public card QR is not the code. Code ownership is not cryptographic proof of ongoing physical-card ownership; the NFT and card can later be sold separately. State this clearly.

**Model C — Persistent physical/digital pair (advanced, not recommended at launch):** NFC secure element or tamper-resistant identifier with challenge-response, plus custody/transfer/repair/reissue procedures. This can demonstrate possession of a chip, not guarantee the cardboard is genuine, undamaged, or inseparable from the chip. It cannot prevent separation of NFT and physical ownership without custody or a specialized protocol and commercial trust assumptions. Cost and support burden are substantial.

**Recommendation:** ship A first. Pilot B only after digital redemption has been audited and support capacity exists. Avoid C unless the physical market clearly demands authenticated high-value objects.

### 20.4 Digital NFT and physical print relationships
- `card_definition_id`: immutable gameplay identity (e.g. DTCG-G111-001).
- `ruleset_version` / `card_text_version`: tournament interpretation; printed version and public errata registry.
- `art_master_id` / `art_hash`: versioned image master; print-ready CMYK derivatives remain traceable to the master.
- `digital_edition_id`: specific Doginal collectible and immutable edition attributes.
- `physical_sku`, `print_run_id`, `print_serial` (optional): manufacturing identifiers, NOT blockchain ownership proof.
- `claim_allocation_id`, `claim_status`, `claim_receipt_hash` (only Model B): entitlement state and independently verifiable supply accounting.
- `paired_edition_id` (optional): historical association, not a guaranteed permanent ownership link.

**Never map a common printed card 1:1 to an existing scarce NFT by default.** Printing a character's image does not create an NFT edition. Public supply dashboards must distinguish digital Genesis editions, physical print runs, and claimable editions. Never advertise an unlimited physical reprint as a limited digital edition.

### 20.5 Suggested future physical products
1. **Learn-to-play box:** two balanced 30-card starter decks, playmat, counters, rules, no randomized contents, no wallet requirement.
2. **Faction decks:** six fixed-list decks; easy onboarding and competitive testing.
3. **Booster packs:** randomized physical cards only after retailer economics, collating, rarity transparency, and draft/sealed design are validated.
4. **Collector editions:** premium print treatments, alternate art, numbered packaging, no mechanical advantage.
5. **Event kit:** playmats, judge guides, deck registration sheets, organized-play promos and tournament policies.

The existing digital five-card Genesis Pack should **not** be assumed to be a good physical draft pack. Five-card packs may work for collecting but likely need a different physical limited-play format or larger product configuration. Test distribution and draft math before choosing pack size.

### 20.6 Print design requirements
- Build a separate card-frame renderer around the same art master; never burn text into the original transparent character image.
- Use standard trading-card dimensions only after vendor selection; typical poker-size reference is 63 x 88 mm (approximately 2.5 x 3.5 in), but vendor tolerances and bleed requirements govern final files.
- Print proofs: CMYK conversion, ICC profiles, ink limits, 300 dpi at final size, bleed/safe zone, line thickness, foil registration, black-detail retention, color-blind icon distinctions, legibility under ordinary indoor lighting, and scratch/rub tests.
- The current highly detailed black/white artwork may lose texture in print. Create a print-specific tonal master and test on matte and coated stocks; do not assume screen render equals print proof.
- Physical backs must be identical and opaque across rarity/print runs in sanctioned decks, including when sleeved; no edge/finish clues that leak hidden card identity.
- Text and icon sizes must survive production tolerances; perform real-life hand-size usability tests.
- Confirm art-generation and reference licenses permit commercial print, resale, packaging, promotional use, and derivative editions; record provenance per card.

### 20.7 Digital-first commercial decision gates (suggested, not observed)
**Gate T0 — Digital game fit:** >=90 days of stable production, sustained non-incentivized returning players, robust retention cohort analysis, repeat deck experimentation, no unresolved P0/P1 gameplay/security issues. No fixed DAU threshold is meaningful without acquisition economics.
**Gate T1 — Tabletop parity prototype:** at least 200 supervised tabletop matches, multiple skill levels, >=90% of observed matches finish without judge intervention, and a documented comparison of digital vs tabletop rule outcomes. Thresholds are initial acceptance hypotheses.
**Gate T2 — Demand:** independently collected waitlist, refundable preorder or nonbinding purchase-intent research, local game store interviews, price testing, and evidence customers want *playable* cards rather than only NFT-linked merch.
**Gate T3 — Unit economics:** vendor quotes at 3 print quantities, landed COGS, fulfillment, returns, distributor/retailer margin, damaged stock, VAT/GST/PST or applicable taxes, duties, storage, working capital, and break-even scenarios. No revenue projection without quotes and demand data.
**Gate T4 — Compliance:** consumer product safety/labeling, advertising, privacy, minors, sweepstakes/gambling/randomized-pack law as applicable, IP and trademark clearance, payment processing, customs, refunds, event prize policies, and cross-border tax advice.
**Gate T5 — NFT claim pilot (optional):** external audit, issuance cap proof, code secrecy, concurrency and fraud controls, account recovery policy, customer support runbook, and disclosures that physical and digital title can diverge.

### 20.8 Physical-to-digital claim protocol — conceptual, not trustless
1. Publish signed manifest for eligible physical SKU, print-run range, claim allocations, NFT edition supply cap, terms, and expiry (if any) before sale.
2. Securely manufacture unique random claim secrets; hash or HMAC commitments in issuer database; never place secrets in visible QR or public metadata. Use tamper-evident concealment and vendor access controls.
3. Buyer uncovers claim secret and signs in with an account/wallet. Server validates entitlement, expiration, status, and anti-abuse limits; rate-limit and detect compromised code batches.
4. Atomically reserve one allocation in the issuer database using unique constraint/idempotency key; persist redemption intent and wallet target.
5. Issue NFT through an audited, bounded Doginal mint process, record chain transaction and finality policy, and settle claim to DELIVERED only after indexer confirmation. Support recoverable `RESERVED`, `MINT_PENDING`, `REORG_PENDING`, `DELIVERED`, `FAILED_RETRYABLE` states.
6. Publish claim receipts without revealing secrets or personally identifying data; reconcile every minted edition to a single allocation and one accepted redemption.
7. Dispute/recovery process handles damaged seals, lost codes, reseller transfers, stolen codes, wrong wallet, chain reorganizations, and provider outage. Some disputes cannot be resolved cryptographically; disclose issuer discretion.

**Threats to test:** photographed QR, guessed codes, insider leaks, duplicate code printing, factory overrun, forged cards, stolen shipment, redemption racing, database rollback, wallet mismatch, phishing, resale after redemption, lost secret, unconfirmed chain mint, reorg, and issuer insolvency. This is a centrally operated entitlement system with on-chain delivery unless a stronger mechanism is separately designed and audited.

### 20.9 Organized play and secondary markets
- Define sanctioned format, legal printings, proxy policy, banned/restricted list, errata precedence, match clock, slow-play, sleeves, deck checks, sideboards (if any), judge appeals, tie/draw resolution, and accessibility accommodations.
- A physical card remains tournament legal even when its NFT counterpart is owned by another wallet. No wallet checks at physical events.
- Physical resale is a separate market from Doginal trading. A paired product listing must explicitly state whether it includes (a) physical card, (b) digital edition, or (c) both, and how delivery is secured.
- If physical and digital assets are bundled, prefer independently verified escrow and shipping/payment protections. Avoid claiming an on-chain transaction enforces real-world shipping.
- Tournament rewards should prioritize trophies, promos, recognition, and merchandise; review cash/crypto prize structures for applicable law.

### 20.10 Compatibility and release QA suite
Add physical QA cases in `DOGE_TCG_PHYSICAL_QA_MATRIX.csv`. Required evidence: prototype print-run ID, ruleset hash, card text version, tabletop board photos, annotated action transcript, digital engine replay of equivalent state, tester skill level, judge interventions, error classification, and pass/fail.

**Hard stop criteria:** tabletop rule cannot be completed without server; unbounded manual bookkeeping; a printed card's meaning differs materially from canonical rules without a documented physical format exception; physical printing changes competitive power by edition; public QR grants NFT claim; repeat claim succeeds; print-back leakage; undeclared card substitution; inaccurate scarcity claims; or a materially unprofitable manufacturing order.

### 20.11 Roadmap and decision
**Now:** add `physical_compatibility` and `manual_bookkeeping_cost` to the 111-card schema; ensure all 18 prototype cards can be resolved with paper, counters, and a two-page reference. Preserve card identity and layered art masters.
**After online success:** paper proxy tournament -> professional print proofs -> 200-match physical parity pilot -> fixed-deck preorder validation -> small physical run.
**Only after that:** randomized physical boosters, retail distribution, and optional redemption-linked premium products.

**Recommendation: reserve the right to go physical without obligating the project to do so.** The primary digital product must stand on its own. The safest long-term bridge is shared game identity, interoperable card art and rules, optional collectibles, and independent physical ownership—not pretending cardboard and Doginals are inherently the same asset.
