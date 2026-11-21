# Existing stack integration inventory

Filled from the live pack on 2026-11-21. Adapters stay in `doginals.lol` and `dogex`. This repo does not mint.

| Component | Existing repo/path | Commit | API / schema / tests | Status | Adapter owner |
| --- | --- | --- | --- | --- | --- |
| doginals.lol `/drops/dogetcg/` | `dogestack/doginals.lol` `src/pages/drops/drop-page-client.tsx`, `src/features/drops/dogetcg-kit.tsx` | `30c5f93f` | Drop kit `dogetcg`. Route already mounted. Play and mint tabs are on that page. | VERIFIED | doginals.lol |
| Pack ripping | `dogenals/spec/protocols/dogetcg/spec.md` and `dogex/src/indexer/updater/dogetcg.rs` | spec `6ab47a19`, dogex `6e4f5be` | `op` set/pack/rip/card/art. Spend of the pack outpoint is the authorization. | VERIFIED | dogex |
| Indexer and card ownership | `dogex` `/api/dogetcg/state`, `/api/dogetcg/pack/{id}` | `6e4f5be` | Reads `dogetcg/*` meta keys. Reorg drops those keys. | VERIFIED | dogex |
| Wallet/auth/signing | `doginals.lol/src/lib/broadcast/doginals-commit-reveal.ts` via Dig local approval | `c2693e16` | Commit then reveal. No public relay. | VERIFIED | doginals.lol |
| Marketplace/DMP | Collection parent builder in `doginals.lol/src/lib/drops/dogetcg/builders.ts` | `c2693e16` | Parent is a ÐMP `collection`. Sale of a sealed pack is an ordinary Doginal transfer. Listing flow is the existing inscription page. | PARTIAL | doginals.lol |
| drok.lol art generation | `drok/` and `scripts/generate_doge_art.py` | drok not pinned here | No dogetcg provider call. Site uses `/drops/dogetcg/cards/*.svg`. | MISSING | drok, later |

## Contract test minimum

dogex unit tests cover the odds document and the pull caps (`dogex/src/dogetcg.rs`). They do not cover a live reorg, a duplicate rip, or a card inscribed by a stranger. Those stay in the indexer path and are not claimed as passing here.
