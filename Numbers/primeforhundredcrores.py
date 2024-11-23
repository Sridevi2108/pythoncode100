import math
def largestprime(n):
    if n % 2==0 or n%5==0:
        return False
    for i in range(3,int(math.sqrt(n)),2):
        if n%i==0:
            return False
    return True
def largestprimenum(n):
    for i in range(n,1,-1):
        if largestprime(i):
            return i
    return None
n=1000000000
result=largestprimenum(n)
print(result)