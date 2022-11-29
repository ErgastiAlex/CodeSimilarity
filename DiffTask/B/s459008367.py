N,M=map(int,input().split())
P=10**9+7
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
a=factorization(M)
ans=1
for x in a:
    c=1
    for i in range(x[1]):
        c*=(N+x[1]-i-1)
    for i in range(x[1]):
        c//=(i+1)
    ans*=c
    ans=ans%P
if M==1:
    ans=1
print(ans)