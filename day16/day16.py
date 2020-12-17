from collections import defaultdict
from functools import reduce
from input import FIELDS,YOUR,NEARBY

#print(FIELDS)
#print(YOUR)
#print(NEARBY)

def valid(nn):
  for _,v in FIELDS.items():
    for a,b in v:
      if a<=nn and nn<=b: return True
  return False

invalid = 0
VALIDNEARBY = []
for n in NEARBY:
  allvalid = True
  for nn in n:
    if not valid(nn):
      invalid+=nn
      allvalid = False
  if allvalid: VALIDNEARBY.append(n)

print("1--->",invalid)

options = {f:set(range(len(YOUR))) for f in FIELDS.keys()}

def validate(i,value):
  for field,ranges in FIELDS.items():
    for a,b in ranges:
      if a<=value and value<=b: break
    else: options[field].discard(i)

for n in VALIDNEARBY:
  for idx,value in enumerate(n):
    validate(idx,value)

mapping = {}
while True:
  found = None
  for k,v in options.items():
    if len(v) == 1:
      found = k
      break
  else: break
  foundv = list(options[found]).pop()
  mapping[found] = foundv
  for k in options:
    options[k].discard(foundv)
print(mapping)


ret = 1
for k,v in mapping.items():
  if k.startswith("departure"):
    ret *= YOUR[v]
    print(v, YOUR[v], ret)

print("2--->",ret)
