from collections import defaultdict

INPUTS= [
 #[0,3,6],
 #[1,3,2],
 [15,12,0,14,3,1],
]

def play(input, target):
  #m = defaultdict(tuple)
  m = [()] * 30000000
  for n,x in enumerate(input):
    m[x] = ((n,n))
    last = x
  while n < target-1:
    n+=1
    last = m[last][-1]-m[last][-2]
    m[last] = (m[last][-1], n) if m[last] else (n,n)
    if not n%1000000: print(n)
  return last

for INPUT in INPUTS:
  print("-->",play(INPUT, 2020), '[', INPUT, 2020)
  print("-->",play(INPUT, 30000000), '[', INPUT, 30000000)
