#!/usr/bin/python3

print('''This example is using the idiomatic stars of the python 3.
Stars is helping to bring together more than one items in the same list.''')

def get_shape(matrix):
    return [len(r) for r in matrix]

def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    shape_of_matrix = get_shape(matrices[0])
    if any(get_shape(m) != shape_of_matrix for m in matrices):
        raise ValueError("Given matrices are not the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]

print('''This add function add items in a matrices line by line.
|[1 1]|   |[2 2]|   |[1+2 1+2]|
|[3 3]| + |[5 5]| = |[3+5 3+5]|
|[7 7]|   |[0 0]|   |[7+0 7+0]|
''')
matrix1 = [[1,1],[3,3],[7,7]]
matrix2 = [[2,2],[5,5],[0,0]]

print(matrix1)
print(matrix2)
print("adding both")
print(add(matrix1,matrix2))

