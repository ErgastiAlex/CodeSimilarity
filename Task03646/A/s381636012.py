def ceil(a,b): return (a+b-1)//b
K=int(input())
print(50)
Y = ceil(K,50)*50
A=[49 + Y//50]*50
for _ in range(Y-K):
    for i in range(49):
        A[i]+=1
    A[-1]-=50
    A.sort()
print(*A)