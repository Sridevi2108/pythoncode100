def selectionsort(arr):
    for i in range(len(arr)-1):
        min_arr=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_arr]:
                min_arr=j
        if min_arr!=i:
            arr[i],arr[min_arr]=arr[min_arr],arr[i]
if __name__=='__main__':
    elements=['sri','apple','ball','elephant','srinithi','mala','raju','srivasthan','viji']
    selectionsort(elements)
    print(elements)
