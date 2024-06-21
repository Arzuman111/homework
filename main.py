def matrix(a,b):
    row_a = len(a)
    col_a = len(a[0])
    c = [[0 for m in range(col_a)] for m in range(row_a)]
    for i in range(row_a):
        for j in range(col_a):
            c[i][j]= a[i][j] * b[i][j]
    return c

a = [[1,2,3],
     [5,6,7],
     [9,10,11]]
b = [[2,4,5],
     [7,10,25],
     [3,5,8]]

c = matrix(a,b)
print(c)
