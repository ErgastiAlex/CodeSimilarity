K = int(input())
N = 50
A = [i for i in range(N)]
q, r = divmod(K, N)
for i in range(N): A[i] += q
for i in range(r):
    for j in range(N):
        if j == i: A[j] += N
        else: A[j] -= 1
print(N)
print(*A)