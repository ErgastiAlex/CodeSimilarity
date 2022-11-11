K = int(input())

N = 50
a = [N-1]*N
d = K//N
m = K % N
for i in range(N):
    a[i] += d

for i in range(m):
    for j in range(N):
        if j == i:
            a[j] += N
        else:
            a[j] -= 1
print(N)
print(' '.join(map(str, a)))

