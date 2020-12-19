import re
from functools import lru_cache
from input import R,I

def getres(l):
  return ''.join(map(getre, l))

@lru_cache(maxsize=None)
def getre(n):
  r = R[n]
  if isinstance(r,str): return r
  return '('+'|'.join(map(getres, r))+')'

print('1--->',
 len(list(filter(lambda i:re.fullmatch(getre(0),i), I)))
)

R[1000]=[[1008,1011]]
R[1008]=[[42],[42,42],[42,42,42],[42,42,42,42],[42,42,42,42,42],[42,42,42,42,42,42],[42,42,42,42,42,42,42]]
R[1011]=[[42,31],[42,42,31,31],[42,42,42,31,31,31],[42,42,42,42,31,31,31,31],[42,42,42,42,42,31,31,31,31,31]]

print('2--->',
 len(list(filter(lambda i:re.fullmatch(getre(1000),i), I)))
)
