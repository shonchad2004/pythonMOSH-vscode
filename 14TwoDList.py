#             A.   2-D Lists
'''
A 2D list (two-dimensional list) in Python is a list of lists. Think of it as a grid or table, where data is organized in rows and columns.

For example, this represents a 2D list:

matrix = [
    [1, 2, 3],  # Row 1
    [4, 5, 6],  # Row 2
    [7, 8, 9]   # Row 3
]

Here:

matrix[0] refers to the first row: [1, 2, 3]
matrix[1][2] refers to the element in the second row, third column: 6
'''

#            B.   CREATING a 2D List
'''
1.  matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

2.  You can create a 2D list with specific dimensions using a nested list comprehension:

rows, cols = 3, 3
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(matrix)

# Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

'''

#       C.  Iterating Through a 2D List
'''
for row in matrix:
    for element in row:
        print(element, end=" ")
        
# Output: 1 2 3 4 5 6 7 8 9
'''
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for rows in matrix:
    for elements in rows:
        print(elements,end=", ")

#  TypeError = list indices must be integers or slices, not tuple.
'''
list indices can be integers (e.g., matrix[1] to access the element at 2nd position.)
can also be slices (e.g., matrix[0:3] to access the indices 0,1&2)

but, can't be a tuple ( e.g., matrix[(1,2)] or matrix[(5,)] )
'''