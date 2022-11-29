import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

M = 10**9+7
N = n+10

g1 = [None] * (N+1) 
g2 = [None] * (N+1) 
inverse = [None] * (N+1) 
g1[0] = g1[1] = g2[0] = g2[1] = 1
inverse[0], inverse[1] = [0, 1] 

for i in range( 2, N + 1 ):
    g1[i] = ( g1[i-1] * i ) % M 
    inverse[i] = ( -inverse[M % i] * (M//i) ) % M # ai+b==0 mod M <=> i==-b*a^(-1) <=> i^(-1)==-b^(-1)*aより
    g2[i] = (g2[i-1] * inverse[i]) % M 

def cmb(n, r, M):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return (g1[n] * g2[r] * g2[n-r]) % M

ans = 0
for ind in range(n):
    ans += a[ind] * cmb(ind, k-1, M)
    ans -= a[n-1-ind] * cmb(ind, k-1, M)
    ans %= M
print(ans%M)