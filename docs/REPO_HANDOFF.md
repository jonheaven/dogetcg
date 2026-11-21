# How to hand off to Cursor

1. Create `github.com/jonheaven/dogetcg` as an empty repository (no generated README/license).
2. Extract the downloadable ZIP, commit its **contents** at repository root, and push.
3. Open `dogetcg` in Cursor. Grant Cursor access to the actual existing codebases (private repos need explicit access).
4. In Agent mode: "Read AGENTS.md, docs/BUILD_PLAN.md, docs/architecture/INTEGRATION_MATRIX.md and all design assets. Start with read-only AS-IS reconnaissance. Verify existing metaprotocol, wallet, indexer, marketplace, and drok.lol tools. Do not rebuild them. Propose normative rules and an 18-card vertical slice. Implement only after recording verified interfaces and unresolved decisions. No mainnet writes or deployments without approval."
5. Require milestone PRs and test evidence. Do not allow autonomous production deployments.

Note: this starter includes no verified source code from private existing infrastructure and does not automatically connect to your other repositories.
