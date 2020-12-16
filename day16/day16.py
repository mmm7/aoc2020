from collections import defaultdict
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


options = {}
for i in range(len(YOUR)):
  options[i]=set(FIELDS.keys())

def validate(i,nn):
  for k,v in FIELDS.items():
    for a,b in v:
      if a<=nn and nn<=b: break
    else: options[i].discard(k)

for n in VALIDNEARBY:
  for i,nn in enumerate(n):
    validate(i,nn)

#print(options)

optionsr = defaultdict(set)
for k,v in options.items():
  for vv in v:
    optionsr[vv].add(k)

#print(optionsr)

res = {}
while True:
  found = None
  for k,v in optionsr.items():
    if len(v) == 1:
      found = k
      break
  if not found: break
  foundv = list(optionsr[found]).pop()
  res[found] = foundv
  for k in optionsr:
    optionsr[k].discard(foundv)

print(res)

ret = 1
for k,v in res.items():
  if k.startswith("departure"):
    ret *= YOUR[v]
    print(v, YOUR[v], ret)

print("2--->",ret)
