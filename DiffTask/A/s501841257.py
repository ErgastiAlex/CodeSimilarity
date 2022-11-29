N,K = map(int,input().split())
MOD = pow(10,9)+7

def cmb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  return fac[n]*finv[r]*finv[n-r]%p

fac = [-1]*(N+1); fac[0] = 1; fac[1] = 1 
finv = [-1]*(N+1); finv[0] = 1; finv[1] = 1 
inv = [-1]*(N+1); inv[0] = 0; inv[1] = 1
for i in range(2,N+1):
  fac[i] = fac[i-1]*i%MOD
  inv[i] = MOD - inv[MOD%i]*(MOD//i)%MOD
  finv[i] = finv[i-1]*inv[i]%MOD

A = list(map(int,input().split()))
A.sort()
ans = 0
for i in range(N):
  MIN = cmb(N-1-i,K-1,MOD)
  MAX = cmb(i,K-1,MOD)
  #print(i,A[i],MAX,MIN)
  temp = A[i]*(MAX-MIN)
  ans = (ans+temp)%MOD
print(ans%MOD)