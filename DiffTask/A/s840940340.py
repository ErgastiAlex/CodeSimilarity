n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
mod = 10**9+7

max_num = 0
min_num = 0

def cmb(n, r, mod):
    if (r<0 or r>n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

g1 = [1, 1] 
g2 = [1, 1] 
inverse = [0, 1] 

for i in range(2, n+1):
    g1.append( (g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

for i in range(k-1,n):
    cmb_num = cmb(i, k-1, mod)
    max_num += cmb_num*a[i] % mod
    min_num += cmb_num*a[n-1-i] % mod
print((max_num-min_num)%mod)
