n=21
num=len(str(n))
temp=n
count=0
while(n>0):
    r=n%10
    count=count+r
    n=n//10
if temp%count==0:
    print("Yes")
else:
    print("No")