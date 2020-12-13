import sys

I=[]

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  I.append((line[0], int(line[1:])))
