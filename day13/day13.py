from math import gcd
from functools import reduce

from input import BUSES,T

def lcm(a,b):
  return a*b//gcd(a,b)
assert lcm(6,10)==30

print(T,BUSES)

wait=[]
for b,_ in BUSES:
  w = (-T)%b
  wait.append((w, b, w*b))

wait.sort()
print(wait)
print("A:",wait[0][2])

def coll(a,b):
  am,ar = a
  bm,br = b
  t=0
  while True:
    step = max((ar-t)%am, (br-t)%bm)
    if not step: return (lcm(am,bm), t)
    t+=step

assert coll((6,2),(10,0))==(30,20)
assert coll((7,2),(5,2))==(35,2)

print(reduce(coll,BUSES))
