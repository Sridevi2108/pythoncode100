n=10 # no.of students
r=6 # no of seats
nfact=1
nr=1
for i in range(1,n+1):
    nfact=nfact*i
for i in range(1,(n-r)+1):
    nr=nr*i
npr=nfact/nr
print(int(npr))