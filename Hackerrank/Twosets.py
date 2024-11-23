a=[2,6]
b=[24,36]

def lcm(x,y):
    mult=x*y
    lcm=mult//gcd(x,y)
    return lcm
def gcd(x,y):
    if x<y:
        x,y=y,x
    while(y!=0):
        r=x%y
        x=y
        y=r
    hcf=x
    return hcf


