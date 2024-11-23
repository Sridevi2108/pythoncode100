a,b=36,27
c=a
d=b
if a<b:
    a,b=b,a
while b!=0:
    rem = a%b
    a=b
    b=rem
hcf = a
mult=c*d
lcm=mult//hcf
print(lcm)