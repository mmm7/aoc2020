import sys
from collections import deque
from input import I

def sumtwo(l, x):
  ll = sorted(l)
  i,j = 0, len(ll)-1
  while i<j:
    if ll[i]+ll[j]==x: return True
    if ll[i]+ll[j]<x: i+=1
    else: j-=1
  return False

assert sumtwo([1,2,3], 5)
assert not sumtwo([1,2,3], 6)
assert not sumtwo([1,2,5], 4)
assert sumtwo([3,1,2], 3)
assert not sumtwo([1], 2)


WS=int(sys.argv[1])
w = deque(I[:WS])

for x in I[WS:]:
  if not sumtwo(w, x): target=x
  w.append(x)
  w.popleft()

print(target)

i,j,s = 0,1,I[0]

while s != target:
  if s < target:
    s,j = s+I[j],j+1
  if s > target:
    s,i = s-I[i],i+1

print("sum=",s)
print(i,j,max(I[i:j])+min(I[i:j]))
