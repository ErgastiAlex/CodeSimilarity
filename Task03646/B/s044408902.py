K = int(input())

N = 50
a = [K//N + i for i in range(N)]

for i in range(K % N):
    a[i] += N + 1
for i in range(N):
    a[i] -= K % N
    
print(N)
print(*a)