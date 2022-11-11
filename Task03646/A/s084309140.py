K = int(input())
N = 50
a = [N-1+K//N]*N
idx = 0

for _ in range(K%N):
    for i in range(N):
        if i==idx:
            a[i] += N
        else:
            a[i] -= 1

    idx += 1

print(N)
print(*a)