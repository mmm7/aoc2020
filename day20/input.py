import numpy as np
import sys

T={}
E={}

lines = [x.strip() for x in sys.stdin]

def _dec(c):
  return (0,1)[c=='#']

def _vectors(m):
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
    #print(l)
    if not l: break
    img.append(list(map(_dec,l)))
  imm = np.array(img)
  #print(img,'\n',imm)
  T[tile] = imm
  E[tile] = list(_vectors(imm))
  imm=np.transpose(imm)
  T[-tile] = imm
  E[-tile] = list(_vectors(imm))
