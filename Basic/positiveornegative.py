num=int(input("Enter a number"))
# using brute force
'''if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("Zero")'''

#using nested if
'''if num>=0:
    if num==0:
        print("zero")
    else:
        print("+ve")

else:
    print("Negative")'''

#using ternary operator
print("+ve" if num>=0 else "-ve")
