from functools import lru_cache
from input import I

@lru_cache(maxsize=None)
def num(col):
  res = 1
  if col not in I: return res
  for c,n in I[col].items():
    res += n* num(c)
  return res

print(num('shiny gold'))
