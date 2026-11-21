#!/usr/bin/env python3
"""Validate repository seed assets and inventory counts; no external dependencies."""
from pathlib import Path
import json,csv,hashlib
R=Path(__file__).resolve().parents[1]
M=json.loads((R/'data/art/GENESIS_111_ART_MANIFEST.json').read_text(encoding='utf-8'))
cards=M['cards']; assert len(cards)==111, f'art cards: {len(cards)}'
print('art cards:',len(cards),'unique ids:',len(set(c.get('card_id',c.get('id')) for c in cards)))
assert len(set(c.get('card_id',c.get('id')) for c in cards))==111
for name,expected in [('DIGITAL_TEST_MATRIX.csv',144),('PHYSICAL_TEST_MATRIX.csv',71)]:
 with (R/'data/qa'/name).open(encoding='utf-8-sig',newline='') as f: count=sum(1 for _ in csv.DictReader(f))
 print(name,count); assert count==expected
for p in sorted((R/'references').glob('*.png')):
 print(p.name,hashlib.sha256(p.read_bytes()).hexdigest()[:16])
assert len(list((R/'references').glob('*.png')))==2
print('PASS: source bundle inventory. No gameplay or security tests executed.')
