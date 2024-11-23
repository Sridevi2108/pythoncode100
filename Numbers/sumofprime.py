n=30
lst=[]
for i in range(1,n):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count = count+1
    if count==2:
        lst.append(i)
for i in range(len(lst)):
    for j in range(i+1):
        if lst[i]+lst[j]== n:
            count = 1
            print(lst[i], "and",lst[j] ,"are the prime numbers of ",n)
    if count==0:
        print("No prime numbers can give the sum of")
