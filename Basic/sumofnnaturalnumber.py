n=int(input("Enter a number:"))
#for loop
# sum1=0
# for i in range(n+1):
#     sum1=sum1+i
# print(sum1)

#using formula
# sum1=0
# sum1=n*(n+1)//2
# print(sum1)

#using recursion
def getsum(n):
    if n==1:
        return 1
    return n+getsum(n-1)
print(getsum(n))

