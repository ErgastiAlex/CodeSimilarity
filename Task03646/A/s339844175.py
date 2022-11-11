#17:38
k = int(input())
n = 50
print(n)
p = k // n
q = k % n
a = [49+p for _ in range(50)]
for i in range(q):
  for j in range(50):
    if i == j:
      a[j] += n
    else:
      a[j] -= 1
print(' '.join(list(map(str,a))))