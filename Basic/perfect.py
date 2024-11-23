n=28
count=0
for i in range(1,int(pow(n,0.5))):
    if n%i==0:
        count=count+i
    elif i==n/i:
        count=count+1
    else:
        count+=i+n/i
if count == n:
    print("Yes")
else:
    print("No")

# n=int(input("Enter a number"))
# count = 0
# for i in range(1,n):
#     if n%i==0:
#         count=count+i
#
# if count==n:
#     print("It is a perfect number")
# else:
#     print("It is not a perfect number")
