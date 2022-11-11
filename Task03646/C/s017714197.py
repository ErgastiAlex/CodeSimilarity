K = int(input())
k = K % 50
kk = K // 50
N = [i for i in range(50)]
for i in range(k):
    for j in range(50):
        if i == j:
            N[j] += 50
        else:
            N[j] -= 1
for i in range(50):
    N[i] += kk
print("50")
print(" ".join(map(str,N)))