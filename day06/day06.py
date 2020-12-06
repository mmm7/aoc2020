#h = open('input-t', 'r')
h = open('input', 'r')
m = [x.strip() for x in h.readlines()]


pp1 = set()
pp2 = set(list('abcdefghijklmnopqrstuvwxyz'))

total1, total2 = 0,0

for l in m:
  if not l:
    total1 += len(pp1)
    total2 += len(pp2)
    pp1 = set()
    pp2 = set(list('abcdefghijklmnopqrstuvwxyz'))
    continue
  curr = set(list(l))
  pp1 = pp1.union(curr)
  pp2 = pp2.intersection(curr)


total1 += len(pp1)
total2 += len(pp2)

print(total1, total2)
