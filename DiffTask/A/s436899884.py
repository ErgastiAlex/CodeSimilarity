import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9+7

fac = [1, 1]
f_inv = [1, 1]
inv = [0, 1]

def prepare(n, mod):
    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod//i)) % mod)
        f_inv.append((f_inv[-1] * inv[-1]) % mod)

def cmb(n, r, mod):
    if n < 0 or r < 0:
        return 0
    if r > n:
        return 0

    return fac[n] * f_inv[r] * f_inv[n-r] % mod


def main():
    N,K,*A = map(int, read().split())

    prepare(N+5, MOD)

    A.sort()
    ans = 0
    for i, a in enumerate(A):
        s_i = a * (cmb(i, K-1, MOD) - cmb(N-i-1, K-1, MOD))
        s_i %= MOD
        ans += s_i
        ans %= MOD

    print(ans)    


if __name__ == "__main__":
    main()
