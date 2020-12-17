import numpy as np

import sys

lines = sys.stdin.readlines()
Y=len(lines)
X=len(lines[0])

IL = []
for l in lines:
  if not l: continue
  IL.append([(0,1)[x=='#'] for x in l.strip()])

I = np.array([IL])
I2 = np.array([[IL]])

