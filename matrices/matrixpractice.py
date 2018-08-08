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
