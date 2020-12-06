#!/usr/bin/python3

import re

#h = open('input-t2', 'r')
h = open('input', 'r')
m = [x.strip() for x in h.readlines()]

pp = {}

FULL=sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
NOCID=sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

valid,total = 0,0

for l in m:
  if not l:
    print(pp)
    total += 1
    if list(sorted(pp.keys())) == NOCID:
      print('   ===============+> VALID')
      valid += 1
    pp={}
    print('----------------------------------------------------------------------------------------')
    continue
  for t in l.split():
    k,v = t.split(':')
    if k=="byr":
      if not re.fullmatch('\d\d\d\d', v): continue
      if int(v) < 1920 or int(v) > 2002: continue
    elif k=="iyr":
      if not re.fullmatch('\d\d\d\d', v): continue
      if int(v) < 2010 or int(v) > 2020: continue
    elif k=='eyr':
      if not re.fullmatch('\d\d\d\d', v): continue
      if int(v) < 2020 or int(v) > 2030: continue
    elif k=='hgt':
      if re.fullmatch('1\d\dcm', v):
         if int(v[:3])<150 or int(v[:3])>193: continue
      elif re.fullmatch('\d\din', v):
         if int(v[:2])<59 or int(v[:2])>76: continue
      else:
         continue
    elif k=='hcl':
      if not re.fullmatch('#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]', v): continue
    elif k=='ecl':
      if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: continue
    elif k=='pid':
      if not re.fullmatch('\d'*9, v): continue
    else: continue

    pp[k]=v

print(total, valid)
