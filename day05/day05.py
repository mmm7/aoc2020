import collections

def decode(s):
  row = 0
  for c in s[:7]:
    row *= 2
    if c=='B': row += 1
  seat = 0
  for c in s[7:]:
    seat *= 2
    if c=='R': seat += 1
  return (8*row+seat, row, seat)

assert decode('BFFFBBFRRR')==(567,70,7)
assert decode('FFFBBBFRRR')==(119,14,7)
assert decode('BBFFBBFRLL')==(820,102,4)

h = open('input', 'r')
passes = [decode(x.strip()) for x in h.readlines()]

print(max([x[0] for x in passes]))

rows = set([x[1] for x in passes])
validrows = set([r for r in rows if r-1 in rows and r+1 in rows])
seats = collections.defaultdict(int,{k:127 for k in validrows})

for p,r,s in passes:
  seats[r] &= ~(1 << s)

for r,s in seats.items():
  if s: print(r,s,r*8+s.bit_length()-1)
