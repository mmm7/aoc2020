from input import I

print(I)
Y=len(I)
X=len(I[0])

def g(S,x,y):
  if x<0 or y<0 or x>=X or y>=Y: return False
  if S[y][x]=='#': return True
  return False

ADJ=[[[] for _ in range(X)] for _ in range(Y)]
for y in range(Y):
  for x in range(X):
    for dx in (-1,0,1):
      for dy in (-1,0,1):
        if not dx and not dy: continue
        dist = 0
        while True:
          dist += 1
          xx,yy = x+(dx*dist),y+(dy*dist)
          if xx<0 or xx>=X or yy<0 or yy>=Y: break
          if I[yy][xx] == 'L':
            ADJ[y][x].append((xx,yy))
            break

print(ADJ)

def around(S,x,y):
  return sum([g(S,xx,yy) for xx,yy in ADJ[y][x]])

def business(n):
  if n==0: return 0
  if n<5: return 1
  return 2

assert business(0) == 0
assert business(1) == 1
assert business(3) == 1
assert business(4) == 1
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

#print(new(I))
#print(new(new(I)[0]))

change = True
num = 0
while change:
  I,change,num=new(I)

print(num)
