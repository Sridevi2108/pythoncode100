nums=[1]
var=[]
for i in range(len(nums)):
    if nums[i] not in var:
        var.append(nums[i])
        count = 0
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                count = 1
        if not count:
            print(nums[i])
