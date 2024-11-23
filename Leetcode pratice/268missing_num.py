nums = [0,1]
n=len(nums)
total_Sum=n*(n+1)//2
missing_sum=0
for i in range(len(nums)):
    missing_sum+=nums[i]
missing_number=total_Sum-missing_sum
print(missing_number)