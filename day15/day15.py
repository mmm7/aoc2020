from collections import defaultdict

INPUTS= [
 #[0,3,6],
 #[1,3,2],
 [15,12,0,14,3,1],
]

def play(input, target):
  m = defaultdict(list)
  for n,x in enumerate(input):
    m[x].append(n)
    last = x
  while n < target-1:
    n+=1
    if len(m[last])==1:
      last = 0
    else:
      last = m[last][-1]-m[last][-2]
    m[last].append(n)
    if not n%1000000: print(n)
  return last

for INPUT in INPUTS:
  print("-->",play(INPUT, 2020), '[', INPUT, 2020)
  print("-->",play(INPUT, 30000000), '[', INPUT, 30000000)
