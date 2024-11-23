n=12090
num = 0
if(n==0):
    num = 1
while(n>0):
    var=n%10
    if var==int(0):
        var=1
    n=n//10
    num=num*10+var
print(num)
