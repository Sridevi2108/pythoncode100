def countnoofdigit(n):
    count = 0
    if n==0:
        return 1
    n=abs(n)
    while(n>0):
        val = n%10
        count=count+1
        n=n//10
    return count



n=input("Enter a number to count the number of digits")
n=int(n)
print(countnoofdigit(n))