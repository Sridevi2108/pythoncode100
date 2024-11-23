#frequency of elements in an array
arr=[10,20,30,10,20,20,30]
var=[]
for i in range(len(arr)):
    if arr[i] not in var:
        count = 1
        for j in range(i+1,len(arr)):
            if arr[j]==arr[i]:
                count = count + 1
        print(f"The frequency of element {arr[i]}:",count)
        var.append(arr[i])
print(var)
6