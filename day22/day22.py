from collections import deque
from input import I

print(I)

P = (deque(I[0]), deque(I[1]))

def round(a,b):
  aa,bb = a.popleft(), b.popleft()
  take = [max(aa,bb), min(aa,bb)]
  winner = (a,b)[bb>aa]
  winner.extend(take)

def play(a,b):
  r = 0
  while a and b:
    print('Round:', r)
    r+=1
    round(a,b)

play(P[0], P[1])
print(P)

w = [a*b for a,b in enumerate(reversed(P[0]+P[1]+deque([0])))]
print('1--->', sum(w))
