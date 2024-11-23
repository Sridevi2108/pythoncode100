a = [1, 3, 2]
temp=a[0]
#largest element in an array
for i in range(len(a)-1):
    if a[i]>temp:
        temp=a[i]
print(temp)
