import sys

lines = sys.stdin.readlines()
T = int(lines[0])
BUSES = [(int(x),-m) for m,x in enumerate(lines[1].split(',')) if x!='x']
