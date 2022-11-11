K = int(input())

a = K//50
b = K%50

print (50)
for i in range(49-b):
    print (48 + a -b, end = ' ')
for i in range(b):
    print (48 + a + 50 - (b-1), end = ' ')
print (49 + a - b)