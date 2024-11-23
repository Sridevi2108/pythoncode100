import math
a=1
b=4
c=4
if a==0:
    print("Invalid input")
else:
    d=b*b-(4*(a*c))
    if d>0:
        print("The equation has two roots")
        print((-b + math.sqrt(d))/(2*a))
        print((-b - math.sqrt(d))/(2*a))
    elif d==0:
        print("Roots and Real are same")
        print(-b/(2*a))
    else:
        print("Roots are complex")
        print(-b / (2 * a), "+i",math.sqrt(-d)/(2*a))
        print(-b / (2 * a), "-i",math.sqrt(-d)/(2*a))



