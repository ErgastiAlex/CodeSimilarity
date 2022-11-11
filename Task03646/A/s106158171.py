k=int(input())
n=50
a=[n-1+k//n]*n
m=k%n
for i in range(m):
  a[i]+=n
  for j in range(n):
    if i==j:continue
    a[j]-=1
print(n)
print(*a)