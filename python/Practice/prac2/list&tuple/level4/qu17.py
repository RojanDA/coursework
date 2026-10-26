# How do you use the map function to apply 
# a function to each element of a list?

def squ(x):
    return x**2

num = [1,2,3,4,5]

sq_num = list(map(squ, num))
sq_num1 = list(map(lambda x: x ** 2, num)) # map with lambda function

print(sq_num)
print(sq_num1)