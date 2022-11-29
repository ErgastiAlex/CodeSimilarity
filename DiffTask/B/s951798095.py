import sys
input = sys.stdin.buffer.readline
import copy

def main():
    N,M = map(int,input().split())
    MOD = 10**9+7
    
    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n**0.5//1))+1):
            if temp%i==0:
                cnt=0
                while temp%i==0:
                    cnt+=1
                    temp //= i
                arr.append([i, cnt])

        if temp!=1:
            arr.append([temp, 1])

        return arr
        
    cl = factorization(M)
    
    def combinations(x,y,N):
        fac = [0]*(N+1)
        fac[0],fac[1] = 1,1
        invfac = copy.deepcopy(fac)
        
        for i in range(2,N+1):
            fac[i] = (fac[i-1]*i)%MOD
            
        invfac[-1] = pow(fac[-1],MOD-2,MOD)
        
        for i in range(N,0,-1):
            invfac[i-1] = (invfac[i]*i)%MOD
            
        return (fac[x+y]*invfac[x]*invfac[y])%MOD
        
    ans = 1
    for pr,num in cl:
        ans *= combinations(N-1,num,N+num)
        ans %= MOD
    
    print(ans)
    
if __name__ == "__main__":
    main()
