n,m=map(int,input().split(" "))
for i in range(n//2):
    pattern_count=2*i+1
    pattern=pattern_count*'.|.'
    center=pattern.center(m,'-')
    print(center)
print('WELCOME'.center(m,'-'))
for i in range(n//2-1,-1,-1):
    pattern_count=2*i+1
    pattern=pattern_count*'.|.'
    center=pattern.center(m,'-')
    print(center)

