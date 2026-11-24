# Lazy, reproducible artwork production

`data/art/GENESIS_111_ART_MANIFEST.json` contains 111 draft recipes, not approved final artwork. Each card ID is stable. **Generate only when requested**; do not pre-generate all 111 by default.

1. Freeze gameplay definition and character role before approving a prompt.
2. Map recipe to existing drok.lol image-generation interface after inspecting its source and auth. `scripts/generate_doge_art.py` is an adapter-based runner, **not** a preconfigured provider.
3. Store per output: card ID, art recipe version, rendered prompt, model/provider, seed if supported, reference image hashes, dimensions, RGBA alpha QC, image SHA-256, generation timestamp, human approval and inscription/delegate ID when applicable.
4. Render the character bright, cartoon, and funny: a chubby Shiba, candy colors, a joke in the pose. Grim engraved armor is the wrong set. Keep the card frame, typography, abilities and stats separate from the picture.
5. Never promise pixel-identical regeneration from a prompt across model versions. Preserve original approved bytes, hash and references; regeneration creates a new asset version.
6. No new artwork is minted or delegated until signed off and its provenance recorded.
