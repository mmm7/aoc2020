import sys

lines = sys.stdin.readlines()
i=0

FIELDS = {}
while True:
  l=lines[i].strip()
  i += 1
  if not l: continue
  if l.startswith("your"): break
  ranges = []
  k,v = l.split(':')
  for vv in v.split('or'):
    a,b = vv.split('-')
    ranges.append((int(a.strip()), int(b.strip())))
  FIELDS[k.strip()] = ranges

your = lines[i]
YOUR = [int(x) for x in lines[i].strip().split(',')]
i+=3

NEARBY = []
for l in lines[i:]:
  l=l.strip()
  if not l: continue
  NEARBY.append([int(x) for x in l.strip().split(',')])
