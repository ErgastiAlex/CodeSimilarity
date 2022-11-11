k = int(input())

# n = 50
print(50)

a = [49 + k//50] * 50

for i in range(k % 50):
    a[i] += 50

for i in range(50):
    a[i] -= k % 50

print(' '.join(map(str, a)))