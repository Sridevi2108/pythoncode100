a,b=36,60
if a<b:
    a,b=b,a
while b!=0:
    r=a%b
    a=b
    b=r
hcf = a
print(hcf)