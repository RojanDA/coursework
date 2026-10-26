# Write a program to create a list of squares of numbers 
# from 1 to 10 using list comprehension.

squares = [x**2 for x in range(1, 11)]

for i in squares:
    print(i)