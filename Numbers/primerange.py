n=5
i=0
c=0
while(c<n):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count = count+1

    if count==2:
        print(i)
        c=c+1
    i = i + 1