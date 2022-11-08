x, y = map(int, input().split())

def gcd(x,y):
    if x>=y:
        a = x
        b = y
    else:
        a = y
        b = x

    ans = a%b
    while ans != 0:
        a = b
        b = ans
        ans = a%b

gcd(x,y)
