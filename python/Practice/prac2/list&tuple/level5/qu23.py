# How do you create a generator expression to 
# iterate over the squares of numbers from 1 to 10?

squares_generator = (x**2 for x in range(1, 11))

# Iterate over the squares using the generator
for square in squares_generator:
    print(square)