import sys

from input import OPT, I
from collections import defaultdict
from functools import reduce

#print(OPT)
OPT1=defaultdict(set)

for allerg, sets in OPT.items():
  OPT1[allerg]=reduce(set.intersection, sets)

#print(OPT1)

ALLERGS = dict()

while True:
  for a,i in OPT1.items():
    if len(i)==1:
      ii=next(iter(i))
      ALLERGS[a]=ii
      break
  else:
    break
  for k in OPT1:
    OPT1[k].discard(ii)

print(ALLERGS)

s = 0
for ingreds, allergs in I:
  for i in ingreds:
    if i not in ALLERGS.values(): s+=1

print('1--->',s)

print('2--->', ','.join([v for _,v in sorted([(a,i) for a,i in ALLERGS.items()])]))

"""
'peanuts': {'jrhvk'},
'shellfish': {'jrhvk', 'qjltjd'},
'nuts': {'jrhvk', 'jhsrjlj'},
'eggs': {'lfcppl', 'jrhvk'},
'wheat': {'jrhvk', 'rfpbpn', 'qjltjd'}
'soy': {'qjltjd', 'jrhvk', 'xslr'},
'dairy': {'lkv', 'jrhvk', 'xslr'},
'sesame': {'lfcppl', 'qjltjd', 'lkv', 'zkls'},

'jrhvk', 'qjltjd', 'jhsrjlj', 'lfcppl', 'rfpbpn', 'xslr', 'lkv', 'zkls'

'peanuts': {'jrhvk'},
'shellfish': {'qjltjd'},
'nuts': {'jhsrjlj'},
'eggs': {'lfcppl'},
'wheat': {'rfpbpn'}
'soy': {'xslr'},
'dairy': {'lkv'},
'sesame': {'zkls'},

'dairy': {'lkv'},
'eggs': {'lfcppl'},
'nuts': {'jhsrjlj'},
'peanuts': {'jrhvk'},
'sesame': {'zkls'},
'shellfish': {'qjltjd'},
'soy': {'xslr'},
'wheat': {'rfpbpn'}

#ALLERG = set(['jrhvk', 'qjltjd', 'jhsrjlj', 'lfcppl', 'rfpbpn', 'xslr', 'lkv', 'zkls'])

lkv,lfcppl,jhsrjlj,jrhvk,zkls,qjltjd,xslr,rfpbpn
['lkv', 'lfcppl', 'jhsrjlj', 'jrhvk', 'zkls', 'qjltjd', 'xslr', 'rfpbpn']
"""
