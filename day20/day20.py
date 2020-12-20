import sys
import numpy as np
from collections import Counter,defaultdict

from input import T,E

# E = {2311: [210, 89, 924, 318], -2311: [498, 231, 616, 300], ...
# print(E)

edgecount = Counter([item for sublist in E.values() for item in sublist])

corners=[]
EE=defaultdict(set)
for t,edges in E.items():
  if t>0 and list(map(lambda x: edgecount[x], edges)).count(1)==2: corners.append(t)
  for i,edge in enumerate(edges):
    EE[edge].add((t, i))

print('1--->',np.product(corners))

# EE = {210: {(2311, 0), (-1427, 1)}, 89: {(2311, 1), (3079, 3)}, ...
#print(EE)

def match(E, tr, dir):
  tile,rot = tr
  d = 'WSEN'.index(dir)
  return E[-tile][(d-rot)%4]

_E = {400: [6,7,8,9], -400: [99,88,77,66]}
assert match(_E, (400, 0), 'N')==66
assert match(_E, (400, 0), 'E')==77
assert match(_E, (400, 0), 'S')==88
assert match(_E, (400, 0), 'W')==99
assert match(_E, (400, 1), 'N')==77
assert match(_E, (400, 1), 'E')==88
assert match(_E, (400, 1), 'S')==99
assert match(_E, (400, 1), 'W')==66
assert match(_E, (-400, -5), 'N')==6
assert match(_E, (-400, -5), 'E')==9
assert match(_E, (-400, -5), 'S')==8
assert match(_E, (-400, -5), 'W')==7

# Get (tile, rotation) so that N matches `edge`. Exclude all tiles from `excl`.
def tile_for_edge(EE, edge, excl=None):
  if excl is None: excl = []
  ret = []
  for a,b in EE[edge]:
    if a in excl or -a in excl: continue
    ret.append((a,b))
  assert len(ret)<2
  if not ret: return None
  return ret[0]

_EE = {200: {(5,0),(-3,2)}, 300: {(-5,3),(-2,0)}}
assert tile_for_edge(_EE, 200, [5, 2])==(-3,2)
assert tile_for_edge(_EE, 200, [-5, 2])==(-3,2)
assert tile_for_edge(_EE, 200, [3, 2])==(5,0)
assert tile_for_edge(_EE, 200, [-3, -2])==(5,0)
assert tile_for_edge(_EE, 200, [-3, -5])==None

def tilefn(T):
  def tile(pos):
    t=T[pos[0]]
    for _ in range(pos[1]%4):
      t=np.rot90(t)
    return t[1:-1,1:-1]
  return tile

tlt,tlr = corners[0],0
while not (edgecount[match(E,(tlt,tlr),'N')]==1 and edgecount[match(E,(tlt,tlr),'W')]==1): tlr+=1
print('starting corner:', tlt, E[tlt])
lines = []
line = [(tlt,tlr)]
while True:    # Build map
  while True:  # Build line
    ne = tile_for_edge(EE, match(E, line[-1], 'E'), [line[-1][0]])
    if not ne: break
    line.append((ne[0],(ne[1]+1)%4))
  nxt = tile_for_edge(EE, match(E, line[0], 'S'), [line[0][0]])
  lines.append(np.concatenate(list(map(tilefn(T), line)), axis=1))
  if not nxt: break
  line = [nxt]

board = np.concatenate(lines)
print(board)

# |01234567890123456789|
#0|                  # |
#1|#    ##    ##    ###|
#2| #  #  #  #  #  #   |
MONSTER = np.array([
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
[0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
])

def findmonster(b,m):
  bx,by = b.shape
  mx,my = m.shape
  dx,dy = bx-mx, by-my
  for x in range(dx+1):
    for y in range(dy+1):
      if (np.logical_and(b[x:x+mx, y:y+my], m) == (m!=0)).all():
        b[x:x+mx, y:y+my] += m

for _ in range(2):
  for _ in range(4):
    findmonster(board, MONSTER)
    board = np.rot90(board)
  board = np.transpose(board)

print('2--->', (board==1).sum())
