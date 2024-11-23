# Sort first half in ascending order and second half in descending
arr=[5, 4, 6, 2, 1, 3, 8, 9, 7]
n=len(arr)
temp=arr[0]
rev=[]
for i in range(n):
    min_arr=i
    for j in range(i+1,n):
        if arr[j]<arr[min_arr]:
            min_arr=j
    if min_arr!=i:
        arr[i],arr[min_arr]=arr[min_arr],arr[i]
for i in range(0,n//2+1):
    rev.append(arr[i])
for i in range(n-1,n//2,-1):
    rev.append(arr[i])
print(*rev)





