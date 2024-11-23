arr=[1,1,0,-1,-1]
val=[]
pos=0
neg=0
zero=0
for i in range(len(arr)):
    if arr[i]>0:
        pos+=1
    elif arr[i]<0:
        neg+=1
    else:
        zero+=1
posfrac = pos / len(arr)
negfrac = neg / len(arr)
zerofrac = zero / len(arr)
print(f"{posfrac:.6f}")
print(f"{negfrac:.6f}")
print(f"{zerofrac:.6f}")