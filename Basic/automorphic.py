n=370
# auto=n**2
# divisor=1
# temp=n
# while temp>0:
#     divisor=divisor*10
#     temp=temp//10
# if auto%divisor ==n:
#     print("Yes")
# else:
#     print("No")

#using endswith function
a=str(n)
num=n**2
b=str(num)
if b.endswith(a):
    print("S")
else:
    print("N")

