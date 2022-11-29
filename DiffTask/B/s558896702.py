def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    return arr


def nCr(n,r,mod = 10**9+7):
    r = min(n-r,r)
    numer = denom = 1
    for i in range(1,r+1):
        numer = numer * (n+1-i) %mod
        denom = denom * i % mod
    return numer * pow(denom,mod-2,mod) %mod


n, m = map(int, input().split())
factors = factorization(m)
mod = 10**9 + 7

ans = 1
for factor, count in factors:
    pattern = nCr(count+n-1, count)
    ans *= pattern
    ans %= mod

print(ans)