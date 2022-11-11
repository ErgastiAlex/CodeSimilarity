K = int(input())

c, m = divmod(K, 50)
ans = [49+c]*50
for i in range(m):
    for j in range(50):
        if j == i:
            ans[j] += 50
        else:
            ans[j] -= 1

print(50)
print(*ans)
