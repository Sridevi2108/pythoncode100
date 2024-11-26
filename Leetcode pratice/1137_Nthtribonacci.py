n = 4
a, b, c = 0, 1, 1

for i in range(3,n+1):
    d = a + b + c
    a,b,c=b,c,d
print(d)