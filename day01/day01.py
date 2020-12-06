#!/usr/bin/python3

h = open('input', 'r') 
inp = [int(x.strip()) for x in h.readlines()]
inp.sort()
print(inp)
i=0
j=len(inp)-1
while i<j:
  curr = inp[i]+inp[j]
  if curr==2020:
    print(inp[i],inp[j],inp[i]*inp[j])
    break
  if curr<2020:
    i += 1
  else:
    j -= 1
