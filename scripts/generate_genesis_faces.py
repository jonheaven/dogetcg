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
    "Bright playful cartoon of one chubby Shiba Inu, big sparkling eyes, soft cel shading, "
    "chunky friendly shapes, sunny candy colors, a joke you could put on a sticker. "
    "Plain warm cream background. Full character, centered, no armor, no weapons, no blood, "
    "no dark fantasy, no engraved metal, no text, no letters, no numbers, no logo, "
    "no watermark, no card frame, no extra limbs."
)

# id, name, one visual beat. Names match doginals.lol genesis.ts.
FACES = [
    ("DOGE-01", "Yard Pup", "a tiny shiba pup in a red bandana, bouncing, tongue out, ears flapping"),
    ("DOGE-02", "Much Wow", "a shiba with huge sparkling eyes and a delighted open-mouth smile, confetti in the air"),
    ("DOGE-03", "Mail Run", "a shiba mailman in a cute blue cap, letter held gently in the mouth, trotting"),
    ("DOGE-04", "Tip Jar", "a shiba hugging a glass tip jar stuffed with coins, proud little grin"),
    ("DOGE-05", "Moonwalk", "a shiba in sunglasses sliding backward, one paw up, tiny moon behind"),
    ("DOGE-06", "Kennel Guard", "a round shiba in an oversized yellow raincoat, whistle on a string, very serious about a very small job"),
    ("DOGE-07", "Chain Mascot", "a shiba wearing a chunky plastic gold chain, posing like a mascot, big smile"),
    ("DOGE-08", "Alpha Howl", "a fluffy shiba howling at a bright cartoon moon, cheeks puffed, happy not scary"),
    ("DOGE-09", "Dust Toss", "a sneaky shiba flinging a puff of glitter, winking"),
    ("DOGE-10", "Fee Bump", "a shiba accountant with round glasses, stacking three fat coins, smug"),
    ("DOGE-11", "Such Magic", "a shiba in a starry wizard hat two sizes too big, a sparkle popping from a paw"),
    ("DOGE-12", "Replay", "a shiba hitting a big red replay button with a paw, motion lines, goofy focus"),
    ("DOGE-13", "Diamond Paws", "a shiba showing off paws covered in silly giant diamond stickers, sparkling"),
    ("DOGE-14", "Block Party", "a shiba in a party hat, balloon tied to the tail, confetti everywhere"),
    ("DOGE-15", "Paper Wallet", "a shiba carefully holding a folded paper wallet like a treasure, tongue peeking out"),
    ("DOGE-16", "Cold Nose", "a shiba in a puffy winter hat and scarf, nose pink, tiny snowflake on the head"),
    ("DOGE-17", "Confirmations", "a shiba stamping a paper with a paw-shaped stamp, satisfied nod"),
    ("DOGE-18", "Hashrate", "a shiba in chunky goggles and a tiny propeller beanie, a friendly spinning fan on the back"),
    ("DOGE-19", "Seal of Wow", "a shiba presenting a big round wax seal with a paw print, ceremonial and cute"),
    ("DOGE-20", "Doge Shield", "a shiba peeking over a round wooden shield painted with a smiling shiba face"),
    ("DOGE-21", "Kabosu Coin", "a shiba holding up a giant coin with its own smiling face on it"),
    ("DOGE-22", "Genesis Bone", "a shiba with a comically huge shiny bone, eyes closed in bliss"),
    ("DOGE-23", "Shibe Scroll", "a shiba unrolling a long blank scroll, ink on the nose"),
    ("DOGE-24", "Lucky Koinu", "a tiny charm shiba with a gold bell, sitting like a lucky statue, one eye winking"),
    ("DOGE-25", "First Block", "a shiba sitting on one oversized toy building block, king of the carpet"),
    ("DOGE-26", "Crown of Ð", "a shiba wearing a crooked paper crown, trying to look royal and failing cutely"),
    ("DOGE-27", "Satoshi's Shibe", "a shiba in a cozy traveler hoodie, one coin on the nose, sunrise colors"),
    ("DOGE-28", "To the Moon", "a shiba in a fishbowl space helmet, floating, paws up, big smile"),
    ("DOGE-29", "Much Forever", "a silver-muzzled shiba in a rocking chair, blanket, content smile, still a cartoon"),
    ("DOGE-30", "Wow Genesis", "a shiba popping out of a gift box, party sparkles, the first wow"),
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
