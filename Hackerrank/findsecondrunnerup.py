n = int(input())
arr = map(int, input().split())
arr=list(arr)
arr.sort()
largest=-100
smallest=-100
for i in arr:
    if i>largest:
        secondlargest=largest
        largest=i
print(secondlargest)