from input import I

print(I)

M = {
  'N':(0,1),
  'E':(1,0),
  'S':(0,-1),
  'W':(-1,0),
  'L':(0,0),
  'R':(0,0),
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

heading=(1,0)
pos=(0,0)
print(pos,heading)

for i,d in I:
  M['F'] = heading
  m = M[i]
  pos = (pos[0]+m[0]*d, pos[1]+m[1]*d)
  heading = turn(heading, i, d)
  print("->",i,d,"->",pos,heading)


print(abs(pos[0]) + abs(pos[1]))
