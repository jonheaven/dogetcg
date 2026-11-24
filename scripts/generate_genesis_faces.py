#!/usr/bin/env python3
"""Paint the 30 Genesis faces the practice rip already displays.

Uses drok's Grok Imagine client (grok-imagine-image-2.0). Writes
doginals.lol/public/drops/dogetcg/cards/DOGE-XX.png and skips files
that already exist. The hotseat rules still use the 18 alpha cards;
this set is the collectible pack, not the 111-recipe manifest.

  python generate_genesis_faces.py
  python generate_genesis_faces.py --only DOGE-01
  python generate_genesis_faces.py --force

Reads GROK_API_KEY from the environment or drok/.env. Never prints it.
Low / 1k is about $0.04 per face on xAI.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
STACK = ROOT.parent
DROK = STACK / "drok"
OUT = STACK / "doginals.lol" / "public" / "drops" / "dogetcg" / "cards"

STYLE = (
    "Premium dark-fantasy trading-card illustration of one unmistakable Shiba Inu, "
    "natural muzzle, knowing eyes, etched metal, realistic fur, cross-hatched ink, "
    "warm gold highlights on a near-black ground. Full character, three-quarter pose, "
    "centered, no environment, no floor, no text, no letters, no numbers, no logo, "
    "no watermark, no card frame, no extra limbs."
)

# id, name, one visual beat. Names match doginals.lol genesis.ts.
FACES = [
    ("DOGE-01", "Yard Pup", "a small shiba pup in a sun-faded bandana, mid-bound, ears flying"),
    ("DOGE-02", "Much Wow", "a shiba struck with delight, gold sparks in the fur, mouth open in a wow"),
    ("DOGE-03", "Mail Run", "a shiba courier with a leather satchel and a rolled letter in its teeth"),
    ("DOGE-04", "Tip Jar", "a shiba beside a dented gold coin jar, one paw on the rim"),
    ("DOGE-05", "Moonwalk", "a shiba in a silver moon-cloak, one paw lifted, lunar dust at the heels"),
    ("DOGE-06", "Kennel Guard", "a stocky shiba in a studded collar and a short watch-spear"),
    ("DOGE-07", "Chain Mascot", "a shiba wearing a heavy chain like a sash, proud and still"),
    ("DOGE-08", "Alpha Howl", "a large shiba mid-howl, mane of fur backlit in gold"),
    ("DOGE-09", "Dust Toss", "a sly shiba flinging a fan of glittering dust from one paw"),
    ("DOGE-10", "Fee Bump", "a shiba clerk stacking gold coins higher with a sly grin"),
    ("DOGE-11", "Such Magic", "a shiba magician in a worn cape, a gold sigil hovering over one paw"),
    ("DOGE-12", "Replay", "a shiba turning an hourglass, the same pose echoed faintly behind it"),
    ("DOGE-13", "Diamond Paws", "a shiba with crystalline claws catching gold light"),
    ("DOGE-14", "Block Party", "a festive shiba in a paper crown, confetti of gold flakes"),
    ("DOGE-15", "Paper Wallet", "a shiba guardian clutching a folded parchment wallet to its chest"),
    ("DOGE-16", "Cold Nose", "a shiba in a frost-rimed scarf, breath visible, calm eyes"),
    ("DOGE-17", "Confirmations", "a shiba scribe pressing a wax seal, rings of gold behind it"),
    ("DOGE-18", "Hashrate", "a shiba engineer with brass goggles and a humming gear on its back"),
    ("DOGE-19", "Seal of Wow", "a shiba knight presenting a round gold seal stamped with a paw"),
    ("DOGE-20", "Doge Shield", "a shiba behind a tall kite shield etched with a shiba face"),
    ("DOGE-21", "Kabosu Coin", "a shiba holding up a large gold coin stamped with its own face"),
    ("DOGE-22", "Genesis Bone", "a shiba with an ancient gold-inlaid bone across its paws"),
    ("DOGE-23", "Shibe Scroll", "a shiba unrolling a long blank parchment, ink brush in the other paw"),
    ("DOGE-24", "Lucky Koinu", "a small charm-like shiba with a gold bell collar, lucky and bright"),
    ("DOGE-25", "First Block", "a shiba standing on a single carved stone block, solemn"),
    ("DOGE-26", "Crown of Ð", "a shiba wearing a heavy gold crown, regal and still"),
    ("DOGE-27", "Satoshi's Shibe", "a mythic shiba in a traveler's coat, a single gold coin in its paw, dawn light"),
    ("DOGE-28", "To the Moon", "a shiba leaping upward, a crescent moon behind its shoulders"),
    ("DOGE-29", "Much Forever", "an ancient shiba with silvered muzzle and a calm, endless stare"),
    ("DOGE-30", "Wow Genesis", "a shiba at the start of things, gold light breaking behind a dark silhouette"),
]


def load_key() -> str:
    key = os.environ.get("GROK_API_KEY") or os.environ.get("XAI_API_KEY")
    if key:
        return key.strip()
    env = DROK / ".env"
    if env.is_file():
        for line in env.read_text(encoding="utf-8").splitlines():
            if line.startswith("GROK_API_KEY=") or line.startswith("XAI_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("GROK_API_KEY is not set and drok/.env has no key")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    selected = [row for row in FACES if not args.only or row[0] == args.only]
    if not selected:
        raise SystemExit(f"no face {args.only}")

    sys.path.insert(0, str(DROK))
    from drokimagine.generators.grok_imagine_client import GrokImagineClient

    client = GrokImagineClient(load_key(), rate_limit_delay=1.0)
    OUT.mkdir(parents=True, exist_ok=True)
    for card_id, name, beat in selected:
        dest = OUT / f"{card_id}.png"
        if dest.exists() and not args.force:
            print(f"SKIP {card_id}", flush=True)
            continue
        prompt = f"{STYLE} Character: {name}. {beat}."
        raw_path = dest.with_suffix(".part")
        print(f"PAINT {card_id} {name}", flush=True)
        client.generate_image(
            prompt,
            str(raw_path),
            aspect_ratio="2:3",
            resolution="1k",
            quality="low",
        )
        with Image.open(raw_path) as im:
            im.convert("RGB").save(dest, "PNG")
        raw_path.unlink(missing_ok=True)
        print(f"WROTE {dest}", flush=True)


if __name__ == "__main__":
    main()
