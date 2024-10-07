def selectionsort(arr):
    for i in range(len(arr)):
        min_array=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_array]:
                min_array=j
        if i!=min_array:
            arr[i],arr[min_array]=arr[min_array],arr[i]

if __name__=='__main__':
    test_cases=[
        [78, 12, 34, 9, 8, 12, 5],
        [],
        [4,3,2,1],
        [8,0,7,4]
    ]
    for i in test_cases:
        selectionsort(i)
        print(i)