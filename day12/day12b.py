from input import I

print(I)

M = {
  'N':(0,1),
  'E':(1,0),
  'S':(0,-1),
  'W':(-1,0),
  'L':(0,0),
  'R':(0,0),
  'F':(0,0),
}

def t(heading, dir):
  x,y=heading
  if dir == 'L': return -y,x
  if dir == 'R': return y,-x
  return x,y

assert t((+1,0),'L')==(0,+1)
assert t((-1,0),'L')==(0,-1)
assert t((0,+1),'L')==(-1,0)
assert t((0,-1),'L')==(+1,0)

assert t((+1,0),'R')==(0,-1)
assert t((-1,0),'R')==(0,+1)
assert t((0,+1),'R')==(+1,0)
assert t((0,-1),'R')==(-1,0)

def turn(heading, dir, deg):
  for _ in range(deg//90):
    heading = t(heading, dir)
  return heading

assert turn((+1,0), 'L', 90)==(0,+1)
assert turn((+1,0), 'L', 180)==(-1,0)
assert turn((+1,0), 'L', 270)==(0,-1)

wp=(10,1)
pos=(0,0)
print(pos,wp)

for i,d in I:
  m = M[i]
  wp = (wp[0]+m[0]*d, wp[1]+m[1]*d)
  wp = turn(wp, i, d)
  if i=='F':
    pos = (pos[0]+wp[0]*d, pos[1]+wp[1]*d)
  print("->",i,d,"->",pos,wp)


print(abs(pos[0]) + abs(pos[1]))
