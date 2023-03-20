"""
[
	[0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
]
"""

# matrix n x n
def manual_increment_matrix(n):

	matrix = [ [ None for y in range(n) ] for x in range(n) ]
	counter = 0
	for index, element in enumerate(matrix):
		for nested_index, nested_element in enumerate(element):
			matrix[index][nested_index] = counter + nested_index
		counter += 1
	return matrix

print(manual_increment_matrix(9))