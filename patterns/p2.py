n=4
'''
****           00 01 02 03
*  *           10 11 12 13
*  *           20 21 22 23
****           30 31 32 33

'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()