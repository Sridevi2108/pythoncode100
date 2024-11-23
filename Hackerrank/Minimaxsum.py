arr=[1,2,3,4,5]
val=[]
total=sum(arr)
for i in range(len(arr)):
    val.append(total-arr[i])
m1=max(val)
m2=min(val)
print(m1,m2)
