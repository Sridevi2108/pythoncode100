#smallest elemnt in an array
arr=[2,1,4]
temp=arr[0]
for i in range(len(arr)):
    if arr[i]<temp:
        temp=arr[i]
print("Smallest element in array",temp)