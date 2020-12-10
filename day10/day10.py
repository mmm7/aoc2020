from input import I

d=[0,0,0,1]
c=0

for v in sorted(I):
  d[v-c] += 1
  c=v

print(d[1], d[3], d[1]*d[3])
