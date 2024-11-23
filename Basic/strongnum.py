n=145
temp = n
val = 0
fact = 1
while(n>0):
    r = n%10
    fact = 1
    for i in range(1,r+1):
        fact = fact * i
    val+=fact
    n=n//10
if temp == val:
    print("strong num")
else:
    print("not")
