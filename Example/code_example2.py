def gcd_foo(gcd):

    if gcd[0] < gcd[1]:
        gcd[0], gcd[1] = gcd[1], gcd[0]
    while gcd[1] > 0:
        r = gcd[0] % gcd[1]
        gcd[0] = gcd[1]
        gcd[1] = r

    return gcd[0]


gcd = list(map(int, input().split()))
gcd_foo(gcd)
