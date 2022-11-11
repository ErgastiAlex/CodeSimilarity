#[N-1]*Nから、逆操作をして構築していく。
K = int(input())
N=50 #N=50で固定してやる

ans=[N-1]*N #初期値は全てN-1

d = K//N # 全てにd回の操作をする
r = K % N  #r個には追加で1回操作をする

for i in range(N):
    ans[i] += N*d #d回の操作での増加分
    ans[i] -= d*(N-1) #他の(N-1)この操作に対する減少分

for i in range(r): #r個には追加で一回操作
    ans[i] += N-(r-1)

for i in range(r,N):#残りの奴らは引かれるだけ
    ans[i] -=r
print(N)
print(" ".join(map(str,ans)))
