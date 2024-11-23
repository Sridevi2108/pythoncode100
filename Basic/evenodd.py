#n=int(input())
#brute force

# if n%2 == 0:
#     print("Even")
# else:
#     print("Odd")

#ternary operator

# print("Even" if n%2==0 else "Odd")

def oddeven(num):
    return not num&1
if __name__=="__main__":
    num=int(input())
    if oddeven(num):
        print("Even")
    else:
        print("Odd")


