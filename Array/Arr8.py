#ascending and descending order 
arr=[10,40,20,30]
n=len(arr)
for i in range(n):
    min_arr=i
    for j in range(i+1,n):
        if arr[j]<arr[min_arr]:
            min_arr=j
    if min_arr!=i:
        arr[i],arr[min_arr]=arr[min_arr],arr[i]
print("Ascending order",*arr)
for i in range(n):
    min_arr=i
    for j in range(i+1,n):
        if arr[j]>arr[min_arr]:
            min_arr=j
    if min_arr!=i:
        arr[i],arr[min_arr]=arr[min_arr],arr[i]
print("Descending order",*arr)
