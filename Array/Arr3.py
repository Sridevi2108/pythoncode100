#find the largest and smallest element in an array
arr=[3,4,5,6,2,1]
temp=arr[0]
var=arr[0]
for i in range(len(arr)):
    if arr[i]>temp:
        temp=arr[i]
    if arr[i]<var:
        var=arr[i]
print("Largest & smallest element in array are",temp,var)