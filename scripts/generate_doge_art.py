#!/usr/bin/env python3
"""Generate DOGE TCG art lazily. Requires an explicitly configured image provider adapter.
Provider adapter module must implement generate(prompt, negative_prompt, seed, width, height, reference_paths) -> bytes (PNG).
Usage: python generate_doge_art.py --list
       python generate_doge_art.py --card DTCG-G111-001 --provider-module my_image_adapter
       python generate_doge_art.py --faction Ghostline --provider-module my_image_adapter
       python generate_doge_art.py --all --provider-module my_image_adapter
       python generate_doge_art.py --all --provider-module my_image_adapter --dry-run
"""
import argparse, hashlib, importlib, json, pathlib, sys
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser(); p.add_argument('--card'); p.add_argument('--faction'); p.add_argument('--all',action='store_true'); p.add_argument('--list',action='store_true'); p.add_argument('--dry-run',action='store_true'); p.add_argument('--force',action='store_true'); p.add_argument('--provider-module'); p.add_argument('--reference-dir',default='art/references'); a=p.parse_args()
data=json.loads((ROOT/'DOGE_TCG_ART_MANIFEST.json').read_text()); cards=data['cards']
if a.list:
 for c in cards:print(c['card_id'],c['faction'],c['card_type'],c['card_name'])
 sys.exit(0)
if sum(bool(x) for x in (a.card,a.faction,a.all))!=1:p.error('Select exactly one of --card, --faction, --all')
selected=[c for c in cards if a.all or c['card_id']==a.card or c['faction'].lower()==(a.faction or '').lower()]
if not selected:p.error('No cards matched')
if not a.dry_run and not a.provider_module:p.error('Provide --provider-module; this script never assumes a model or API')
adapter=importlib.import_module(a.provider_module) if not a.dry_run else None
for c in selected:
 dest=ROOT/'art'/'generated'/f"{c['card_id']}.png"; meta=dest.with_suffix('.generation.json')
 if dest.exists() and not a.force:print('SKIP existing',dest);continue
 refs=[str(ROOT/a.reference_dir/f'{r}.png') for r in c['reference_asset_ids']]
 if a.dry_run:print('WOULD GENERATE',c['card_id'],c['card_name'],'refs=',refs);continue
 missing=[r for r in refs if not pathlib.Path(r).is_file()]
 if missing:raise FileNotFoundError(f'Missing reference images for {c["card_id"]}: {missing}')
 output=adapter.generate(prompt=c['prompt'],negative_prompt=c['negative_prompt'],seed=c['seed_hint'],width=c['canvas']['width'],height=c['canvas']['height'],reference_paths=refs)
 if not isinstance(output,bytes):raise TypeError('Adapter must return PNG bytes')
 dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(output)
 with Image.open(dest) as im:
  if im.format!='PNG' or im.mode!='RGBA':raise ValueError(f'{dest} must be RGBA PNG')
  alpha=im.getchannel('A');low,high=alpha.getextrema()
  if low!=0 or high!=255:raise ValueError(f'{dest}: background not fully transparent or subject absent')
  if any(im.getpixel(pt)[3]!=0 for pt in [(0,0),(im.width-1,0),(0,im.height-1),(im.width-1,im.height-1)]):raise ValueError('Subject touches corners')
 sha=hashlib.sha256(output).hexdigest()
 meta.write_text(json.dumps({'card_id':c['card_id'],'prompt_sha256':hashlib.sha256(c['prompt'].encode()).hexdigest(),'art_recipe_version':c['art_recipe_version'],'seed_hint':c['seed_hint'],'sha256':sha,'provider_module':a.provider_module,'reference_paths':refs,'review_status':'unreviewed','note':'Record provider model/version/settings externally before approval. Do not overwrite approved immutable art.'},indent=2)+'\n')
 print('GENERATED',dest,sha)
