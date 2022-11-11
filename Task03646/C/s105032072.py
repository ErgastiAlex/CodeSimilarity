K = int(input())
N = 50
a = [K//N + N-1]*50

for i in range(K%N):
    a[i] += N+1
    for j in range(N):
        a[j] -= 1

print(N)
for i in a:
    print(i,end=" ")
print()
