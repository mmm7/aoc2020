from input import get_masks,get_op

import sys

mem = {}
lines = sys.stdin.readlines()
for l in lines:
  l = l.strip()
  if not l: continue
  if l.startswith('mask'):
    MASKOR,MASKAND = get_masks(l)
  elif l.startswith('mem'):
    addr,val = get_op(l)
    val|=MASKOR
    val&=MASKAND
    mem[addr]=val
  else: assert False, l

print('1--->',sum(mem.values()))
