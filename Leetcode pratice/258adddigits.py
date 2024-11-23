num=199
while(num>=10):
    sum=0
    while(num>0):
        val=num%10
        sum=sum+val
        num=num//10
    num=sum
print(num)




