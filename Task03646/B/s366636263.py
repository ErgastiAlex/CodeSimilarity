k = int(input())

a = [50 - i - 1 for i in range(50)]
div, mod = divmod(k, 50)

for i in range(50):
    a[i] += div

for i in range(mod):
    a[i] += 1

print(len(a))
print(*a)