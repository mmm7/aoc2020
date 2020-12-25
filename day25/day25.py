MOD=20201227
SUBJ=7

A=6930903
B=19716708

# Example:
assert pow(17807724, 8, MOD)==14897079
assert pow(5764801, 11, MOD)==14897079

a,b=1,1
secret = 0
while True:
  if secret%1000000 == 0: print('...',secret)
  if a==A:
    print('a',a,A,secret)
    print('1--->',pow(B,secret,MOD))
    break
  if b==B:
    print('b',b,B,secret)
    print('1--->',pow(A,secret,MOD))
    break
  a = (a*SUBJ)%MOD
  b = (b*SUBJ)%MOD
  secret += 1
