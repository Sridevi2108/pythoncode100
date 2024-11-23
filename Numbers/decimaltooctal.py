n=10
val=[]
reverse=0
while n>0:
    a=n%8
    val.append(a)
    n=n//8
digit=0
for i in val:
    digit=digit*10+i
while digit>0:
    var=digit%10
    reverse=reverse*10+var
    digit=digit//10
print(reverse)