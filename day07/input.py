from collections import defaultdict
import re

h = open('input', 'r')
m = [x.strip() for x in h.readlines()]

I = {}
for l in m:
  en = {}
  m = re.fullmatch('(.*) bags contain (.*)\.', l)
  k = str(m.group(1))
  v = str(m.group(2))
  if v == 'no other bags':
    #I[k] = {}
    continue
  for rule in v.split(','):
    ww = rule.strip().split()
    en[' '.join(ww[1:-1])] = int(ww[0])
  I[k]=en

INV=defaultdict(set)

for o,ii in I.items():
  for i in ii.keys():
    if o not in INV[i]: changed = True
    INV[i].add(o)

#bright gray bags contain 2 bright gold bags, 5 dull lavender bags.
#light purple bags contain 1 faded salmon bag, 5 dim bronze bags, 3 shiny gray bags, 5 dull teal bags.
