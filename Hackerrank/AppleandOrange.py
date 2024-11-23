s,t=7,11
a,b=5,15
m,n=3,2
apples=[-2,2,1]
oranges=[5,-6]
val=[]
val1=[]
applecount = 0
orangecount=0
for i in range(len(apples)):
    v=apples[i]+a
    val.append(v)
for j in range(len(oranges)):
    o=oranges[j]+b
    val1.append(o)
for v in val:
    if s<=v<=t:
        applecount+=1
for v in val1:
    if s<=v<=t:
        orangecount+=1
print(applecount)
print(orangecount)
