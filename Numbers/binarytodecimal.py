num=1001
dec=0
i=0
while(num>0):
    result = num%10
    r=result*(2*i)
    dec=dec+r
    num=num//10
    i=i+1
print(dec)
