def f(k):
    n = 50
    a = [k//n + n-1] * n
    for i in range(k%n):
        for j in range(n):
            if i == j:
                a[j] += n
            else:
                a[j] -= 1
    return a

def solve(k):
    a = f(k)
    print(len(a))
    print(" ".join(map(str, a)))

solve(k=int(input()))