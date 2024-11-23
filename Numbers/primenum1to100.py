n=100

if n==0 or n==1:
    print("Invalid input")
for i in range(2,100):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count = count+1
    if count == 2:
        print(i,end=" ")


