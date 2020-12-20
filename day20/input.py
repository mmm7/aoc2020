import numpy as np
import sys

# { tile: array }
# array is 2D numpy array with 0 and 1.
T={}

# { tile: (edge, edge, edge, edge) }
# Negative tile means flipped.
E={}

lines = [x.strip() for x in sys.stdin]

def _decode(c):
  return (0,1)[c=='#']

def _edges(m):
  for _ in range(4):
    yield int(''.join(map(str,m[:1, 0:][0])), 2)
    m = np.rot90(m)

while True:
  tile = None
  while tile is None and lines:
    line = lines.pop(0)
    if not line: continue
    tile = int(line[4:].strip(' :'))
  if tile is None: break
  #print('======================', tile)
  img = []
  while lines:
    l = lines.pop(0)
    if not l: break
    img.append(list(map(_decode,l)))
  imm = np.array(img)
  T[tile] = imm
  E[tile] = list(_edges(imm))
  imm=np.transpose(imm)
  T[-tile] = imm
  E[-tile] = list(_edges(imm))
