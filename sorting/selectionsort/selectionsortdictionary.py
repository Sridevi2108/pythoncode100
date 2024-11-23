def selectionsort(n):
    arr=list(n.items())
    for i in range(len(arr)-1):
        min_arr=i
        for j in range(i+1,len(arr)):
            if arr[j][1]<arr[min_arr][1]:
                min_arr=j
        if min_arr!=i:
            arr[i],arr[min_arr]=arr[min_arr],arr[i]
    return dict(arr)
if __name__=='__main__':
    elements={'elephant':3,'apple':1,'ball':2,'ant':4}
    sorted=selectionsort(elements)
    print(sorted)
