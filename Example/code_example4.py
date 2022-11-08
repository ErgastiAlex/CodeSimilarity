def gcd(y, x):
  if y < x:
    x, y = y, x

  while x > 0:
    r = y % x
    y = x
    x = r

  return x

y, x = map(int, input().split())
print(gcd(y, x))

