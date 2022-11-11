

K = int(input())
N = 50

A = [49] * 50

for i in range(N):
    A[i] += K // 50

for i in range(K % N):
    A[i] += 51
    for j in range(N):
        A[j] -= 1

print(N)
print(*A)