import sys


# https://www.redblobgames.com/grids/hexagons/#coordinates-cube
# Axial Coordinates
C = {
  'e':  (1,0),
  'se': (0,1),
  'sw': (-1,1),
  'w':  (-1,0),
  'nw': (0,-1),
  'ne': (+1,-1),
}

I = []
for l in sys.stdin:
  l=l.strip()
  if not l: continue
  i = []
  while l:
    for k,v in C.items():
      if l.startswith(k):
        l = l[len(k):]
        i.append(v)
        break
    else:
      assert False, l
  I.append(i)
