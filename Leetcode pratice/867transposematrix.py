matrix = [[1,2,3],[4,5,6],[7,8,9]]
m1=[]

for i in range(len(matrix[0])):
    new_row = []
    for j in range(len(matrix)):
        new_row.append(matrix[j][i])
    m1.append(new_row)
print(m1)