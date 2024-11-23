n=100
m=500
for i in range(n,m):
    temp = i
    val=0
    num=len(str(i))
    while(temp!=0):
        r=temp%10
        val=val+r**num
        temp=temp//10
    if val == i:
        print(i)