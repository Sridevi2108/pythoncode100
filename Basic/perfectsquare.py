import math
n=int(input())
# num = math.sqrt(n)
# if num==int(num):
#     print("Yes")
# else:
#     print("no")

#using ceil and floor function
if(math.ceil(math.sqrt(n)))==(math.floor((math.sqrt(n)))):
    print("Yes")
else:
    print("No")