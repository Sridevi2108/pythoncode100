n1,d1=map(int,input("Enter num & den of first number").split(" "))
n2,d2=map(int,input("Enter num & den of first number").split(" "))
add1= n1*d2
add2=n2*d1
fraction=(add1+add2)
print(fraction,"/",d1*d2)