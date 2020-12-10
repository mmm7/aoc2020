from input import I

D=3
I.sort()
print(I)
N=len(I)

def idx(x): return (x+D)
dp=[0]*(N*D)



dp[idx(0)]=1

for v in I:
  dp[idx(v)] = sum(dp[idx(v)-3:idx(v)])

print(dp,dp[idx(v)])
