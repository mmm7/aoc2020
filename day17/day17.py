import numpy as np
from itertools import product

from input import I

print(I)
print(I.shape)


def l(x): return max(x-1,0)
def h(x): return x+2

def cube(S,x,y,z):
  return S[l(x):h(x),l(y):h(y),l(z):h(z)]

def curr(S,x,y,z):
  if x<0 or y<0 or z<0: return 0
  try:
    return S[x,y,z]
  except IndexError:
    return 0

def rules(curr, neigh):
  return 1 if curr and neigh==2 or neigh==3 else 0

def step(S):
  X,Y,Z = S.shape
  NS = np.zeros([X+2,Y+2,Z+2])
  for x,y,z in product(range(X+2), range(Y+2), range(Z+2)):
        neigh = np.sum(cube(S,x-1,y-1,z-1))
        c = curr(S,x-1,y-1,z-1)
        NS[x,y,z] = rules(c, neigh-c)
  return NS

S = I
for i in range(6):
  S = step(S)
  print(i, np.sum(S))

print("------->1:",np.sum(S))
