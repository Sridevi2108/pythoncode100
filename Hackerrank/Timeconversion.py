s='01:01:00 PM'
def Timechanger(s):
    if s[-2:]=='AM' and s[:2]=='12':
        return '00'+ s[2:8]
    elif s[-2:]=='AM':
        return s[0:8]
    elif s[-2:]=='PM' and s[:2]=='12':
        return s[0:8]
    else:
        return str(int(s[:2])+12)+s[2:8]
print(Timechanger(s))
