N, M = map(int, input().split())
MOD = 10**9+7
MAX = 10**6
if M==1:
    print(1)
    exit()
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            # arr.append([i, cnt])
            arr.append(cnt)
    if temp!=1:
        arr.append(1)

    if arr==[]:
        arr.append(1)

    return arr

arr = factorization(M)
def COMinit():
    """
    逆元テーブルをつくる前処理
    計算量はO(n)
    1 <= k <= n <= 1e7程度
    p: 素数
    """
    fac = [0]*MAX
    finv = [0]*MAX
    inv = [0]*MAX

    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[0], inv[1] = 1, 1
    for i in range(2, MAX):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD
    return fac, finv, inv


def comb(n, k):
    """
    nCk mod MODを求める.
    この部分はO(1)
    """
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return int(fac[n] * (finv[k] * finv[n-k] % MOD) % MOD)

def perm(n, k):
    """
    nPk mod MOD
    """
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return int((fac[n] * finv[n-k])%MOD)
fac, finv, inv = COMinit()

ans = 1
for k in arr:
    ans *= comb(N+k-1, k)
    ans %= MOD
print(ans)