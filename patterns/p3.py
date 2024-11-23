n=4

'''
 ****        00 01 02 03
  ****          11 12 13 14
    ****           22 23 24 25
     ****             33 34 35 36

'''
for i in range(n):
    for j in range(n):
        if i==j or i<=j:
            print((i,j),end=" ")
            j=j+1
        else:
            print(" ",end=" ")
    print()