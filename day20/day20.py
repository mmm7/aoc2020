from collections import Counter,defaultdict

from input import T,E

print(E)

c = Counter([item for sublist in E.values() for item in sublist])
print(c)

singles=defaultdict(int)

for t,edges in E.items():
  for edge in edges:
    if c[edge]==1 and t>0:
      singles[t]+=1

print(singles)

res = 1
for t,s in singles.items():
  if s==2: res*=t
print('1--->',res)
