from collections import defaultdict
import re
import sys


I=[]

for line in sys.stdin:
  line = line.strip()
  I.append([line[:3], int(line[3:])])
