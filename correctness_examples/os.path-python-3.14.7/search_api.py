"""Search generated API names, signatures and descriptions; imports no target package."""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('query', nargs='?', default='')
parser.add_argument('--limit', type=int, default=20)
args = parser.parse_args()
if args.limit < 1:
    parser.error('--limit must be positive')
root = Path(__file__).resolve().parent
rows = json.loads((root / 'api_index.json').read_text(encoding='utf-8'))
terms = args.query.casefold().split()
matches = [r for r in rows if all(t in (' '.join(str(r.get(k) or '') for k in ('qualified', 'signature', 'summary'))).casefold() for t in terms)]
matches.sort(key=lambda r: (r['qualified'].rsplit('.', 1)[-1].casefold() != args.query.casefold(), r['qualified'].count('.'), r['qualified']))
for item in matches[:args.limit]:
    print(item['qualified'])
    print('  ' + (item.get('signature') or 'Signature unavailable'))
    print('  ' + item['summary'])
    print('  ' + str(root / item['page']))
print(f'{len(matches)} matches; showing {min(len(matches), args.limit)}')
