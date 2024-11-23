a=[17,28,30]
b=[99,16,8]
bob=0
alice=0
for i in range(len(a)):
        if a[i]>b[i]:
            bob+=1
        if b[i]>a[i]:
            alice+=1
print(bob,alice)
