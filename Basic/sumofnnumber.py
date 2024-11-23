n=int(input())
def addsum(n):
    if n==0:
        return n
    return n+addsum(n-1)
print(addsum(n))