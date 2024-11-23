import calendar
n=int(input())
# if n%400 == 0 or (n%4==0 and n%100!=0):
#     print("leap")
# else:
#     print("not")


#using calender module
# if calendar.isleap(n):
#     print("leap")
# else:
#     print("Not")

#using lambda
is_leap_year=lambda n:(n%4==0 and n%100!=0) or (n%400==0)
if is_leap_year(n):
    print("leap")
else:
    print("not")



