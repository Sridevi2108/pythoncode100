year = 2021
month = 4
if (month==2) and (year % 4==0) and (year % 100!=0) or (year % 400==0):
    print("29 days")
elif(month==2):
    print("28 days")
elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("31 days")
else:
    print("30 days")
