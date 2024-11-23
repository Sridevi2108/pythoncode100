# nums = [0,1,0,3,12]
# lst=[]
# count = 0
# for i in range(len(nums)):
#     if nums[i]==0:
#         count = count + 1
#     else:
#         lst.append(nums[i])
# # lst.extend([0]*count)
# # print(lst)
# for i in range(count):
#     lst.append(0)
# print(lst)
nums=[0,1,0,3,12]
n=len(nums)
index=0
for i in range(n):
    if nums[i]!=0:
        nums[index]=nums[i]
        index+=1
for i in range(index,n):
    nums[i]=0
