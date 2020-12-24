from functools import reduce
from collections import defaultdict
import operator
from input import I,C

#print(I)

tiles = defaultdict(int)

for i in I:
  x,y = (0,0)
  for dx,dy in i:
    x,y = x+dx, y+dy 
  print((x,y))
  tiles[(x,y)] = 1-tiles[(x,y)]

print(tiles)
print('1--->', sum(tiles.values()))

def step(tiles):
  votes=defaultdict(int)
  for t,black in tiles.items():
    if not black: continue
    votes[t] += 0
    for c in C.values():
      votes[(t[0]+c[0], t[1]+c[1])] += 1
  #print(votes)
  newtiles = defaultdict(int)
  for pos,v in votes.items():
    if tiles[pos]:
      newtiles[pos] = not(v==0 or v>2)
    else:
      newtiles[pos] = v==2
  return newtiles

for i in range(100):
  tiles = step(tiles)
  #print(i, sum(tiles.values()))

print('2--->', sum(tiles.values()))
