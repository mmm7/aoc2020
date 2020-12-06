#!/usr/bin/python3

h = open('input', 'r')

m = [x.strip() for x in h.readlines()]

Y=len(m)
X=len(m[0])

def slope(dx,dy):
    ret=0
    x,y=0,0

    while y<Y:
      #print(m[y], x, y)
      if m[y][x]=='#': ret += 1
      elif m[y][x]!='.': assert False
      x = (x+dx)%X
      y += dy
    return ret

res = 1
for x,y in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
  s = slope(x,y)
  res *= s
  print(x,y,s, res)

