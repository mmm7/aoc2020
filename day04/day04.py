#!/usr/bin/python3

#h = open('input-t', 'r')
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
    if list(sorted(pp.keys())) == NOCID: valid += 1
    pp={}
    continue
  for t in l.split():
    k,v = t.split(':')
    if k!="cid":
      pp[k]=v

print(total, valid)
