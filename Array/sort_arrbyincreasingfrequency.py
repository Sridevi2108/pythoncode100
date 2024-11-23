nums=[1,1,2,2,2,3]
lst=[]
for i in range(len(nums)):
    count = 1
    if nums[i] not in lst:
        for j in range(i+1,len(nums)):
            if nums[j]==nums[i]:
                count = count +1
    print(f"The frequency of element {nums[i]}",count)
    lst.append(nums[i])
print(lst)
