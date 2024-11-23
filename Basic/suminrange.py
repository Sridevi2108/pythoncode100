#sum of numbers in given range
n=int(input("Enter n"))
m=int(input("Enter m"))
# sum=0
# for i in range(n,m+1):
#     sum=sum+i
# print(sum)

# using formula

# sum1=0
# sum1=((m*(m+1)//2) - (n*(n+1)//2))+n
# print(sum1)

#using recursion
def rec_sum(n,m):
    if n>m:
        return 0
    return n + rec_sum(n+1,m)
print(rec_sum(n,m))


