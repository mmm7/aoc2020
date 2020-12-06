#!/usr/bin/python3

h = open('input', 'r') 
inp = [int(x.strip()) for x in h.readlines()]

N=len(inp)

two = []
for i in range(N):
  for j in range(N):
    two.append((inp[i]+inp[j], inp[i], inp[j]))

inp.sort()
two.sort()

i=0
j=len(two)-1
while i<len(inp) and j>=0:
  curr = inp[i]+two[j][0]
  if curr==2020:
    print(inp[i],two[j])
  if curr<2020:
    i += 1
  else:
    j -= 1
