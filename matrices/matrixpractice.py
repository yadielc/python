'''
matrixpractice.py

Here is some practice problems for
matrices in Python.

'''
mv = [
    [5, 10, 2, 6, 1]
]

mv

# assign vector to a 5x1 matrix
vT = [
    [5],
    [10],
    [2],
    [6],
    [1]
]
vT

#multiplying by a scalar

r = []
for i in range(len(m)):
    row = m[i]
    new_row = [] # empty row for now
    for j in range(len(row)):
        m_ij = m[i][j]
        r_ij = 5 * m_ij
        new_row.append(r_ij)
    r.append(new_row)
r

#print a matrix
def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            m_ij = matrix[i][j]
            print(m_ij, '\t', end="")
        print('\n') # prints a new line
    return

m = [
    [8, 7, 1, 2, 3],
    [1, 5, 2, 9, 5],
    [8, 2, 2, 4, 1]
]

matrix_print(m)
