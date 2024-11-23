n=828282
v=2
count = 0
while(n>0):
    val=n%10
    if val==v:
        count = count+1
    n=n//10
print(count)