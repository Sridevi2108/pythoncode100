n=2
arr=[]
for i in range(n):
    arr.append([])
lastAnswer=0
Answers=[]
queries=[[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
for i in queries:
    qtype,x,y=i
    if qtype==1:
        idx=(x^lastAnswer)%n
        arr[idx].append(y)
    elif qtype==2:
        idx=(x^lastAnswer)%n
        pos=y%len(arr[idx])
        lastAnswer=arr[idx][pos]
        Answers.append(lastAnswer)
print(Answers)