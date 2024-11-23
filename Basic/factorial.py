n=10
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(n))

#using for loop
fact=1
if n==0:
    print("1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(fact)