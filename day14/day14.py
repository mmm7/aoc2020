from input import get_masks,get_op

import sys

mem = {}
lines = sys.stdin.readlines()
for l in lines:
  l = l.strip()
  if not l: continue
  if l[:4] == 'mask':
    MASKOR,MASKAND = get_masks(l)
  elif l[:3] == 'mem':
    addr,val = get_op(l)
    val|=MASKOR
    val&=MASKAND
    mem[addr]=val

s = 0
for _,v in mem.items():
  s+=v

print(s)
