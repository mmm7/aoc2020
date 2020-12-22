import sys

I = []
for l in sys.stdin:
  l = l.strip()
  if not l: continue
  if l.startswith('Player'):
    I.append([])
    continue
  I[-1].append(int(l))
