import re

def get_mask(l):
  m = re.fullmatch('mask = (.*)',l.strip())
  return str(m.group(1))

def get_masks(l):
  smask = get_mask(l)
  return (int(smask.replace('X','0'), 2), int(smask.replace('X','1'), 2))

MASKOR,MASKAND = get_masks('mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
assert MASKOR==64, MASKOR
assert MASKAND==68719476733, MASKAND

def get_op(l):
  m = re.fullmatch('mem\[(.*)\] = (.*)', l.strip())
  return(int(m.group(1)), int(m.group(2)))

