x1=43
v1=3
x2=70
v2=2
if v1==v2:
    if x1==x2:
        print("Yes")
    else:
        print("No")
else:
    distance=(x2-x1)/(v1-v2)
    if(distance>0 and distance%1==0):
        print("Yes")
    else:
        print("No")

