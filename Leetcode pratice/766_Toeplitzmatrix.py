matrix=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
for i in range(1,len(matrix)):
    for j in range(1,len(matrix)):
        if matrix[i][j] != matrix[i - 1][j - 1]:
            print("F")
print("T")