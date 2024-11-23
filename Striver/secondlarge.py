arr=[12,35,1,10,34,1]

for i in range(len(arr)-1):
    min_arr = i
    for j in range(i+1,len(arr)):
        if arr[min_arr] == arr[i + 1]:
            print(-1)
        if arr[j]<=arr[min_arr]:
            min_arr = j
    if i!=min_arr:
        arr[i],arr[min_arr]=arr[min_arr],arr[i]
print(arr)
second_large=arr[-2]
print("The second largest element",second_large)

