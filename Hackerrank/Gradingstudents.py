grades=[73,67,38,33]
result=[]
for i in range(len(grades)):
    if grades[i] < 38:
        result.append(grades[i])
    else:
        inital_grade=grades[i]
        while grades[i] % 5 != 0:
            grades[i] = grades[i] + 1
        if grades[i]-inital_grade < 3:
            result.append(grades[i])
        else:
            result.append(grades[i])
print(result)



