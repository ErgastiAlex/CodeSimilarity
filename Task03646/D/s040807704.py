N = 50
K = int(input())
x = K%N
ls = [0]
for i in range(N-1):
  ls += [ls[-1]+1]
for i in range(x):
  ls[i] += N
  for j in range(N):
    if j!=i:
      ls[j] -= 1
ans = [(K-x)//N+c for c in ls]
print(N)
print(*ans)
