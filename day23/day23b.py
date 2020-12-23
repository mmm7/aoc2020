STEP=10000000
N=1000000

#IS="54321"
#IS="716892543"
#IS="389125467"
#N=9

IS="716892543"

I = list(map(lambda c:int(c)-1, IS))
LI = len(I)

#print(IS, I, LI)

S = [None] * N

def left(p, t):
  a,b = p
  return (t,b)

def right(p, t):
  a,b = p
  return (a,t)

for x in range(N):
  S[x] = ((x-1)%N, (x+1)%N)

for i in range(LI):
  S[I[i]] = (I[(i-1)%LI], I[(i+1)%LI])

if N>LI:
  S[I[0]]=left(S[I[0]], N-1)
  S[N-1]=right(S[N-1], I[0])

  S[I[LI-1]]=right(S[I[LI-1]], LI)
  S[LI]=left(S[LI], I[LI-1])

###############################################################

def l(x): return S[x][0]
def r(x): return S[x][1]

def step(curr):
  sl = r(curr)
  sc = r(sl)
  sr = r(sc)
  #print('   sec:', sl+1,sc+1,sr+1)
  nextcurr = r(sr)
  dest = (curr-1)%N
  while dest in [sl,sc,sr]: dest=(dest-1)%N
  # Remove
  S[l(sl)], S[r(sr)] = right(S[l(sl)], r(sr)), left(S[r(sr)], l(sl))
  # Insert
  insl = dest
  insr = r(dest)
  S[insl] = right(S[insl], sl)
  S[insr] = left(S[insr], sr)
  S[sl] = left(S[sl], insl)
  S[sr] = right(S[sr], insr)
  return nextcurr

def _prints(s, curr):
  return
  def enc(i): return str(i+1)
  lnorm = []
  lrev = []
  cc = curr
  cr = l(curr)
  for _ in range(N):
    lnorm.append(cc)
    lrev.append(cr)
    cc=r(cc)
    cr=l(cr)
  assert cc==curr, (cc,curr)
  print('  curr:',curr+1)
  print(''.join(map(enc,lnorm)))
  print(''.join(map(enc,reversed(lrev))))

curr=I[0]
_prints(S,curr)

for st in range(STEP):
  if st%500000 == 0: print(st)
  _prints(S,curr)
  curr = step(curr)

print('2--->', (r(0)+1)*(r(r(0))+1))
