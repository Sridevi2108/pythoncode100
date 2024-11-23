#second smallest element in array
arr=[4,2,5,6,7,8,1]
for i in range(len(arr)-1):
    min_arr = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_arr]:
            min_arr=j
    if min_arr !=i:
        arr[i],arr[min_arr]=arr[min_arr],arr[i]
print("Second smallest element in array:",arr[1])



