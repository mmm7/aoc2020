from input import I

print(I)
Y=len(I)
X=len(I[0])

def g(S,x,y):
  if x<0 or y<0 or x>=X or y>=Y: return False
  if S[y][x]=='#': return True
  return False

def around(S,x,y):
  ret = 0
  for dx in (-1,0,1):
    for dy in (-1,0,1):
      if dx or dy: ret+=g(S,x+dx,y+dy)
  return ret

def business(n):
  if n==0: return 0
  if n<4: return 1
  return 2

assert business(0) == 0
assert business(1) == 1
assert business(3) == 1
assert business(4) == 2
assert business(5) == 2

STATE_MACHINE = {
 '.': '...',
 'L': '#LL',
 '#': '##L',
}

def new(S):
  change = False
  num = 0
  NS=[(['.']*X) for _ in range(Y)]
  for y in range(Y):
    for x in range(X):
       curr = S[y][x]
       n = STATE_MACHINE[curr][business(around(S,x,y))]
       if n=='#': num += 1
       if n!=curr: change=True
       NS[y][x] = n
  return NS,change,num

change = True
num = 0
while change:
  I,change,num=new(I)

print(num)
