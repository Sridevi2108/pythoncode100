#n=10
# a,b=0,1
# print(a,b,end=" ")
# for i in range(n):
#     c=a+b
#     print(c,end=" ")
#     b=a
#     a=c

# using recursion
def fibbo(i):
    if i<=1:
        return i
    else:
        return fibbo(i-1)+fibbo(i-2)

n=10
for i in range(n):
    print(fibbo(i))