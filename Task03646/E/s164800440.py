k=int(input())
x=[0]*50
k1=k//50
k2=k%50
for i in range(k2):
    x[k2-i-1]=50-i
for i in range(k2+1,50):
    x[i]=i-k2
for i in range(50):
    x[i]+=k1
print(50)
print(" ".join(map(str,x)))
