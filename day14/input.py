import re

def get_mask(l):
  m = re.fullmatch('mask = (.*)',l.strip())
  return str(m.group(1))

def get_masks(l):
  smast = get_mask(l)
  MASKOR,MASKAND = 0,0
  for c in smask:
    MASKOR <<= 1
    MASKOR += (0,1)[c=='1']
    MASKAND <<= 1
    MASKAND += (0,1)[c!='0']
  return (MASKOR,MASKAND)

MASKOR,MASKAND = get_masks('mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
assert MASKOR==64

def get_op(l):
  l = l.strip()
  m = re.fullmatch('mem\[(.*)\] = (.*)', l)
  v = 0
  return(int(m.group(1)), int(m.group(2)))

