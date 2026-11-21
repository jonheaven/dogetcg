#!/usr/bin/env python3
"""Read-only integrity checks for supplied design artifacts; no chain/network access."""
import csv, json, pathlib, collections, sys
root=pathlib.Path(__file__).resolve().parent
fail=[]
def check(cond,msg):
 print(('PASS' if cond else 'FAIL'),msg)
 if not cond: fail.append(msg)
manifest=json.loads((root/'DOGE_TCG_ART_MANIFEST.json').read_text(encoding='utf-8'))
cards=manifest['cards']; ids=[c.get('card_id') for c in cards]
check(len(cards)==111,'111 art recipes')
check(len(set(ids))==111,'unique card IDs')
check(all(c.get('prompt') and c.get('negative_prompt') and c.get('art_recipe_version') for c in cards),'complete basic art recipes')
check(all(c.get('card_type') in {'Unit','Tactic','Relic'} for c in cards),'known card types')
check(collections.Counter(c['card_type'] for c in cards)=={'Unit':69,'Tactic':30,'Relic':12},'69 Units / 30 Tactics / 12 Relics')
check(set(c['faction'] for c in cards)=={'Ironclad','Outriders','Ghostline','Ashbound','Runekeepers','Wildpack','Neutral'},'six factions plus Neutral')
check(all(c.get('approved_asset_sha256') in (None,'') for c in cards),'no final art falsely marked approved')
for name,count in [('DOGE_TCG_QA_TEST_MATRIX.csv',144),('DOGE_TCG_PHYSICAL_QA_MATRIX.csv',71)]:
 with (root/name).open(newline='',encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
 check(len(rows)==count,f'{name}: {count} inventoried scenarios')
check((root/'DOGE_TCG_GENESIS_BLUEPRINT.md').exists(),'blueprint included')
print('\nRESULT:', 'FAILED' if fail else 'ARTIFACT INTEGRITY OK — NOT GAMEPLAY/SECURITY VALIDATION')
sys.exit(bool(fail))
