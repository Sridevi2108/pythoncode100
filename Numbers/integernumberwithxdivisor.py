N=7
c=0
for i in range(1,N+1):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        c=c+1
print(c)

