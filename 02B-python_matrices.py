'''Creating a matrix'''

# n_of_columns = int(input('columns?'))
# n_of_rows = int(input('rows?'))
# matrix = []
# for i in range(n_of_rows):
#     r = []
#     while len(r) != n_of_columns:
#         r = list(map(int, input('enter a row of length >> ' + str(n_of_columns) + '\n').split()))
#     matrix.append(r)
# print(matrix)

'''Adding two matrices'''

matrix0 = [[1,2,3],[4,5,6],[7,8,9]]

matrix1 = matrix0
matrix2 = matrix0
add = []
for row in range(len(matrix0)):
    row1 = []
    for column in range(len(matrix0[0])):
        element = matrix1[row][column] + matrix2[row][column]
        row1.append(element)
    add.append(row1)
print(add)
        
'''Multiplying two matrices'''
matrix3 = [[1,2,3],[4,5,6]]
matrix4 = [[7,8],[9,10],[11,12]]
multiply = []
if len(matrix3[0]) == len(matrix4):
    for row2 in range(len(matrix3)):
        row3 = []
        for column2 in range(len(matrix4)):
            element_sum = [matrix3[row2][n] * matrix4[n][column2] for n in range(len(matrix3[0]))]
            row3.append(sum(element_sum))
        multiply.append(row3)
print(multiply)