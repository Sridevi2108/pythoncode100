n=12
temp=0
sum_of_divisor = 0
for i in range(1,n):
    if n%i==0:
        sum_of_divisor+=i
if sum_of_divisor>n:
    print("It is abundant number")
else:
    print("It is not abundant number")
