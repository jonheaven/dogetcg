# DOGE TCG — Genesis 111

**Repository starter and Cursor build contract.** Target: https://doginals.lol/drops/dogetcg/  
Organization: https://github.com/jonheaven  

This repo is the contract: design handoff, 111 art recipes, and the alpha rules in [`docs/RULES.md`](docs/RULES.md). The playable match and the pack page are the storefront at `doginals.lol/drops/dogetcg` (`dogestack/doginals.lol`). Pack sale is not open.

## Start here
1. Read [`AGENTS.md`](AGENTS.md) and [`docs/BUILD_PLAN.md`](docs/BUILD_PLAN.md).
2. Run `python scripts/validate_bundle.py`.
3. In Cursor, provide read access to the existing doginals.lol, drok.lol, indexer, wallet, and metaprotocol source repositories. Record the actual paths and commit IDs.
4. Produce the AS-IS inventory and integration mapping before implementing anything.
5. Build the **deterministic 18-card playable game** before expanding to 111 or producing final art.

## Design status
- 111 **art concepts** exist; 111 balanced **playable card definitions do not**.
- Rules and decisions remain **provisional**; historical blueprint sections can conflict.
- QA matrices list scenarios, **not passing tests**.
- Existing pack-ripping metaprotocol, indexer, wallet, marketplace and drok.lol image generation are **user-reported existing infrastructure**. Reuse them; verify their APIs from source.
- No production transactions, pack issuance, irreversible inscriptions, or deployment without explicit approval.

## Repository layout
- `AGENTS.md` — authoritative coding agent instructions
- `.cursor/rules/` — Cursor rule
- `docs/legacy/` — historical full design blueprint, not normative rules
- `docs/decisions/` — unresolved product decisions
- `docs/architecture/` — source inventory, interfaces, integration design
- `data/art/` — 111 versioned art recipes
- `data/qa/` — 215 proposed QA scenarios
- `references/` — original art reference PNGs
- `scripts/` — validators and art adapter entrypoint

**No claim of audited protocol fairness or security is made.**
