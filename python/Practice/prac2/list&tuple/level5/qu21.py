# How do you use a nested list comprehension to create a 3x3 matrix?

matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]

# Print the matrix
for row in matrix:
    print(row)