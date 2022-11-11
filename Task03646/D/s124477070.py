k=int(input())
n=50
a=[0]*n
cnt=k//n
rest=k%n
for i in range(n):
  a[i]=cnt+i
for i in range(rest):
  for j in range(n):
    if i==j:
      a[j]+=n
    else:
      a[j]-=1
print(50)
print(*a)