arr = [1,2,3,5]
n = len(arr) + 1
num = n * (n + 1) / 2
count=0
for i in range(len(arr)):
    count=count+arr[i]
missingnum = num - count
print(int(missingnum))
