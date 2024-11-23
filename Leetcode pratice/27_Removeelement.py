nums=[3,2,2,3]
val=3
count = 0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[count]=nums[i]
        count+=1
print(count)