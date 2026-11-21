# AS-IS architecture

Recorded 2026-11-21 from the live pack at `C:\Users\jheav\dogestack`. Commit ids are short SHAs at the time of this note.

| Piece | Path | Commit | What it actually is |
| --- | --- | --- | --- |
| Public page | `doginals.lol` route `/drops/dogetcg` | `30c5f93f` | The game’s own page inside the drops router. Play, mint, practice rip, singles, sealed lookup. |
| Pack protocol | `dogenals/spec/protocols/dogetcg/spec.md` | `6ab47a19` | `p: "dogetcg"`. Issuer inscribes the set and every pack. Owner spends the pack to rip, then spends it again per card. Pulls use block `H+1`. |
| Indexer | `dogex/src/dogetcg.rs`, `dogetcg_api.rs`, `indexer/updater/dogetcg.rs` | `6e4f5be` | Same rules. `GET /api/dogetcg/state` and `GET /api/dogetcg/pack/{id}`. |
| Wallet inscribe | `doginals.lol/src/lib/drops/dogetcg/inscribe.ts` | `c2693e16` | P2SH commit then reveal through command.dog. Rip and card reveals spend the pack outpoint and pay it back. |
| Free rules | `doginals.lol/src/lib/drops/dogetcg/alpha.ts` | `30c5f93f` | Hotseat ruleset `dogetcg-alpha-1`. Not inscribed. |
| Art generator | `drok/` | not wired | `scripts/generate_doge_art.py` is still an empty adapter. Faces on the site are SVG placeholders. |

dogex is chain truth (`dogex.command.dog`, local `:8080`). command.dog broadcasts (`api.command.dog`, local `:3000`). Dig (`dig/`, `@dig/web`) signs. The storefront is `doginals.lol`, served on this PC at `:3080`.

The historical blueprint in `docs/legacy/` is not the rules. The 111-card art manifest is not the checklist. The live checklist is 30 Genesis cards in `doginals.lol/src/lib/drops/dogetcg/genesis.ts` (1,000 packs × 5).
