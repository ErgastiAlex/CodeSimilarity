k=int(input())
n=50
a=[0 for _ in range(n)]
for i in range(n):
  if i < (k%n):
    a[i]=n
  else:
    a[i]=n-1-k%n
for i in range(n):
  a[i]+=(k//n)
print(n)
for i in range(n):
  if i==n-1:
    print(a[i])
  else:
    print(a[i],end=" ")