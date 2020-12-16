import re
from itertools import product
from input import get_mask,get_op

import sys

def _binary(s):
  v=0
  for c in s:
    v <<= 1
    v += int(c)
  return v

assert _binary('0')==0
assert _binary('1')==1
assert _binary('10')==2
assert _binary('1010')==10

def _addresses(a, mask):
  addr = bin(a)[2:]
  while len(addr)<36: addr = '0'+addr
  addr = list(addr)
  print(addr)
  ret = []
  pos = []
  ss = []
  for i,c in enumerate(mask):
    if c == '1': addr[i] = 1
    if c == 'X':
      pos.append(i)
  print(mask,pos)
  if not pos: return [_binary(addr)]
  for comb in product('01', repeat=len(pos)):
      for i,c in zip(pos,comb): addr[i]=c
      ret.append(_binary(addr))
  return ret

assert _addresses(64,'000000000000000000000000000000000010')==[66], _addresses(64,'000000000000000000000000000000000010')
assert _addresses(64,'000000000000000000000000000000000X10')==[66,70], _addresses(64,'000000000000000000000000000000000X10')

mem = {}
lines = sys.stdin.readlines()
for l in lines:
  l = l.strip()
  if not l: continue
  if l[:4] == 'mask':
    mask = get_mask(l)
  elif l[:3] == 'mem':
    addr,val = get_op(l)
    for a in _addresses(addr,mask):
      mem[a]=val

s = 0
for _,v in mem.items():
  s+=v

print(s)

