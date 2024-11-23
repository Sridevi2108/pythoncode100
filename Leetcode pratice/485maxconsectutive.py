nums=[1,0,1,1,0,1]
lst = []
count = 0
for i in range(len(nums)):

    if nums[i] == 1:
        count = count + 1
        lst.append(count)

    elif nums[i] == 0:
        count = 0
        lst.append(count)

print(max(lst))