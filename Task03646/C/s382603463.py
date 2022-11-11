k = int(input())
n = 50
d = k%n

a = [49]*n

for i in range(d):
    for j in range(n):
        a[j] -= 1
    a[i] += (n+1)

for j in range(n):
    a[j] += k//n
print(n)
print(*a)