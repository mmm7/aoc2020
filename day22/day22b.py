from collections import deque
from input import I

print(I)

P = (deque(I[0]), deque(I[1]))

def round(a,b):
  aa,bb = a.popleft(), b.popleft()
  if len(a)<aa or len(b)<bb:
    wi = bb>aa
  else:
    wi = play(deque(list(a)[:aa]), deque(list(b)[:bb]), set())
  winner = (a,b)[wi]
  take = [(aa,bb)[wi], (aa,bb)[1-wi]]
  winner.extend(take)

def play(a,b,history):
  r = 0
  while True:
    if not a: return 1
    if not b: return 0
    if ((tuple(a),tuple(b))) in history:
      return 0
    history.add((tuple(a),tuple(b)))
    #print('Round:', r, a,b)
    r+=1
    round(a,b)

print(P)
wi=play(P[0], P[1], set())
winnerdeck=list((P[0],P[1])[wi])
print(wi, winnerdeck)

w = [a*b for a,b in enumerate(reversed(winnerdeck+[0]))]
print('2--->', sum(w))
