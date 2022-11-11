

K = int(input())
N = 50
# 最後の状態からさかのぼる
A = [49] * 50
# K を均等に割り振る（どれか一つを集中して選択しない）
for i in range(N):
    A[i] += K // 50
# 割り振った残りを、さらになるべく均等に割り振る
for i in range(K % N):
    A[i] += 51
    for j in range(N):
        A[j] -= 1

print(N)
print(*A)