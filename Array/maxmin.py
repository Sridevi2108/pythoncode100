n=5
num=[0]*n
for i in range(n):
    a=int(input("Enter a number:"))
    num[i]=a
for i in range(len(num)):
    min_arr=i
    for j in range(i+1,len(num)):
        if num[j]<num[min_arr]:
            min_arr=j
    if min_arr!=i:
        num[i],num[min_arr]=num[min_arr],num[i]
print(num[0])
print(num[n-1])