k=int(input())
n=50
a=[n-1+k//n]*n
for i in range(k%n):
  a[i]+=n
  for j in range(n):
    if i!=j:a[j]-=1
print(n)
print(*a)