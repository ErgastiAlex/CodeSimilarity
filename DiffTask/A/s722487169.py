def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7
N = 10**5  
g1 = [1, 1]  
g2 = [1, 1]  
inverse = [0, 1]  

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)


N, K = map(int, input().split())

A_array = list(map(int, input().split()))

A_array.sort()

ans = 0

for i in range(N - K):
    count = (cmb(N - i, K, mod) + mod - cmb(N - i - 1, K, mod)) % mod
    ans = (ans + A_array[-(i + 1)] * count % mod) % mod
    ans = (ans + mod - A_array[i] * count % mod) % mod
ans = (ans + A_array[K - 1] - A_array[-K]) % mod
print(ans)
