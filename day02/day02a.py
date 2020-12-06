#!/usr/bin/python3

import re
from collections import Counter

RE=re.compile('^(.*)\-(.*) (.): (.*)$')

h = open('input', 'r')

ret = 0
tot = 0
for x in h.readlines():
  tot += 1
  m = RE.match(x.strip())
  mi,ma,ch,s = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
  cnt = Counter(s)
  print(mi,ma,ch,s,cnt[ch], cnt)
  if mi<=cnt[ch] and cnt[ch]<=ma: ret+=1
print(ret, tot)
