n=4
a = 0
b = 1
for i in range(1, n):
    c = b + a
    a = b
    b = c

print(c)