k = int(input())
print(50)
ans = [49 + k // 50 for _ in range(50)]
k %= 50
for i in range(k):
    for j in range(50):
        if i == j:
            ans[i] += 50
        else:
            ans[j] -= 1
print(*ans)