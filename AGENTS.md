# DOGE TCG — Instructions for all coding agents

## Mission
Build a competitive, enjoyable, deterministic DOGE TCG using the owner's **existing** Dogecoin stack, integrated with doginals.lol/drops/dogetcg/. Do not replace functioning infrastructure. Preserve future tabletop playability.

## Source precedence
1. Verified source code, API contracts, tests, and deployed interfaces (record commit hashes).
2. Owner-approved normative ruleset, schema, and card definitions **once created**.
3. `docs/decisions/DECISION_REGISTER.csv` and `docs/BUILD_PLAN.md` for pending decisions.
4. `docs/legacy/GENESIS_BLUEPRINT_v0.5.md` as *historical product intent*, not executable truth.
5. Art manifest is art data, never gameplay authority.
If sources conflict, document the conflict; do not silently guess.

## Non-negotiables
- **Read-only discovery first**: inspect jonheaven repositories, actual doginals.lol source, pack-ripping metaprotocol, wallet, indexer, marketplace, and drok.lol generator. Private code may need explicit local access.
- Existing chain services are integrations, **not TODOs to reinvent**. Use adapters and contract tests.
- Game rules package must be deterministic, pure, versioned, independently replayable, integer-only, and portable to tabletop.
- Ownership and edition rarity never increase competitive stats. Do not gate the core competitive game on holding expensive NFTs.
- Never infer pack odds, randomization, supply limits, signature domain, chain reorg policy, or wallet API from a filename or project name.
- No blockchain writes, mainnet transactions, purchases, irreversible minting, deploys, migrations, or secrets handling without owner approval.
- Treat 111 art recipes as *provisional*; art follows frozen card mechanics. Preserve original references and image hashes.
- Never claim the 215 QA scenarios passed until executed with evidence.

## Work order
1. Produce `docs/architecture/AS_IS.md`, `INTEGRATION_MATRIX.md`, `GAP_ANALYSIS.md`, and `docs/decisions/PROPOSED_RESOLUTIONS.md` with repo paths and commits.
2. Obtain owner approval for the canonical v1 alpha rules; write normative `RULES.md`, schemas, glossary, priority/trigger timing, and example turns.
3. Implement a pure deterministic 18-card vertical slice, CLI/hotseat demo, test vectors, replay verification, and invariants.
4. Add online multiplayer with authoritative server, reconnect, privacy-safe spectator state, and anti-cheat.
5. Expand to all 111 balanced card definitions and automated combination tests.
6. Integrate wallet, ownership, packs, indexer, marketplace using **existing verified APIs**.
7. Integrate drok.lol provider adapter; approve faction anchors, render individual transparent character masters, separate card frame/text from character art.
8. Production security, load, QA, launch approvals. Physical bridge only after online traction.

## Deliverables at each milestone
Code, commands, tests and results, commit SHA, interface changes, known risks, rollback, and owner decisions. Never fabricate evidence. Stop and label blockers explicitly.
