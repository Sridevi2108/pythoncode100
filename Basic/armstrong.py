n=153
num=len(str(n))
temp=n
val=0
while(n>0):
    r=n%10
    val=val+r**num
    n=n//10
if val==temp:
    print("Yes")
else:
    print("No")
