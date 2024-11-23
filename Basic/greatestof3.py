a=9
b=10
c=12
# if(a>b)and(a>c):
#     print(a)
# elif(b>c)and(b>a):
#     print(b)
# else:
#     print(c)

# using nested if statement

# if(a>=b):
#     if (a>=c):
#         print(a)
# elif(b>=c):
#     if(b>=a):
#         print(b)
# else:
#     print(c)

# using ternary
max=a if a>b else b
max=c if c>max else max
print(max)


