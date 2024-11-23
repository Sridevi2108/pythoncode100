a,b=16,32
if a<b:
    a,b=b,a
while b!=0:
    r=a%b
    a=b
    b=r
hcf = a
print(hcf)