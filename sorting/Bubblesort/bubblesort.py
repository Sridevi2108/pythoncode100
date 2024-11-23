def bubblesort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] =  temp
                flag = True
        if flag==False:
            break
    return arr
if __name__=='__main__':
    elements=[1,2,3]
    bubblesort(elements)
    print(elements)
