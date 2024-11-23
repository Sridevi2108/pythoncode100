#n=int(input("Enter a number"))
# brute force method
# temp=n
# r=0
# while(n!=0):
#     val=n%10
#     r=r+val
#     n=n//10
# print(r)

# recursion
n=5678
r = 0
def findsum(n,r):
    if n==0:
        return r
    val=n%10
    r=r+val
    return findsum(n//10,r)
print(findsum(n,r))