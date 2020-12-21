import sys
from collections import defaultdict

OPT = defaultdict(list)
I = []

for l in sys.stdin:
  l = l.strip()
  l = l.replace(')', '').replace(',', '')
  if not l: continue
  ing, allerg = l.split('(contains')
  I.append((ing.split(), allerg.split()))
  for a in allerg.split():
    OPT[a].append(set(ing.split()))
