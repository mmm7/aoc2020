IS="389125467"
IS="716892543"

I = list(map(int,IS))
TOP = max(I)+1

CURR=I[0]

def rot(l, e):
  idx = l.index(e)
  l = l[idx:]+l[:idx]
  return l

def step(l,curr):
  l = rot(l, curr)
  sec = l[1:4]
  print('   sec:', sec)
  l = l[:1]+l[4:]
  sel = (curr-1)%TOP
  while sel not in l:
    sel = (sel-1)%TOP
  l = rot(l,sel)
  l = l[:1]+sec+l[1:]
  return l

def play(l,curr,num):
  while num:
    num-=1
    l=step(l,curr)
    idx=l.index(curr)
    curr = l[(idx+1)%len(l)]
    print(l,curr)
  return l

print(I,CURR)
l=rot(play(I,CURR,100),1)

print(l)
print(l[1:])
print('1--->', ''.join(map(str,l[1:])))
