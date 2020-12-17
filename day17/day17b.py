import numpy as np
from itertools import product

from input import I2 as I

print(I)
print(I.shape)


def l(x): return max(x-1,0)
def h(x): return x+2

def cube(S,x,y,z,w):
  return S[l(x):h(x),l(y):h(y),l(z):h(z),l(w):h(w)]

def curr(S,x,y,z,w):
  if x<0 or y<0 or z<0 or w<0: return 0
  try:
    return S[x,y,z,w]
  except IndexError:
    return 0

def rules(curr, neigh):
  return 1 if curr and neigh==2 or neigh==3 else 0

def step(S):
  X,Y,Z,W = S.shape
  NS = np.zeros([X+2,Y+2,Z+2,W+2])
  for x,y,z,w in product(range(X+2), range(Y+2), range(Z+2), range(W+2)):
        neigh = np.sum(cube(S,x-1,y-1,z-1,w-1))
        c = curr(S,x-1,y-1,z-1,w-1)
        NS[x,y,z,w] = rules(c, neigh-c)
  return NS

S = I
for i in range(6):
  S = step(S)
  print(i, np.sum(S))

print("------->2:",np.sum(S))
