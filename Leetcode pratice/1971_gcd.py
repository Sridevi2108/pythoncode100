nums=[2,5,6,9,10]
a=min(nums)
b=max(nums)
while b!=0:
    r=a%b
    a=b
    b=r
    gcd = a
print(gcd)