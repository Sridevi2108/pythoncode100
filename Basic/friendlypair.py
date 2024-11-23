a,b=6,28
sum_of_divisor_a=0
sum_of_divisor_b=0
for i in range(1,a):
    if a%i==0:
        sum_of_divisor_a=sum_of_divisor_a+i
aratio=sum_of_divisor_a/a

for i in range(1,b):
    if b%i==0:
        sum_of_divisor_b=sum_of_divisor_b+i
bratio=sum_of_divisor_b/b
if aratio==bratio:
    print("Yes ,it is friendly pair")
else:
    print("No, it is not friendly pair")


