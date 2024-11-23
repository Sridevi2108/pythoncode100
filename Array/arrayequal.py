arr1=[1, 2, 5]
arr2=[2,4,15]
if(len(arr1)==len(arr2)):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]!=arr2[j]:
                break
else:
    print("True")