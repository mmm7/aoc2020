import re
from itertools import product
from input import get_mask,get_op

import sys

def _binary(s):
  return int(''.join(s),2)

assert _binary('0')==0
assert _binary('1')==1
assert _binary('10')==2
assert _binary('1010')==10

def _addresses(a, mask):
  addr = list(bin(a)[2:].rjust(36,'0'))
  print(addr)
  pos = []
  for i,c in enumerate(mask):
    if c == '1': addr[i] = '1'
    if c == 'X': pos.append(i)
  print(mask,pos,addr)
  if not pos: return [_binary(addr)]
  ret = []
  for comb in product('01', repeat=len(pos)):
      for i,c in zip(pos,comb): addr[i]=c
      ret.append(_binary(addr))
  return ret

assert _addresses(64,'000000000000000000000000000000000010')==[66], _addresses(64,'000000000000000000000000000000000010')
assert _addresses(64,'000000000000000000000000000000000X10')==[66,70], _addresses(64,'000000000000000000000000000000000X10')

mem = {}
for l in sys.stdin.readlines():
  l = l.strip()
  if l.startswith('mask'):
    mask = get_mask(l)
  elif l.startswith('mem'):
    addr,val = get_op(l)
    for a in _addresses(addr,mask):
      mem[a]=val

print('2--->',sum(mem.values()))
