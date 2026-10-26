import math
# Write a function add that takes two positional arguments
# and returns their sum.
def addition(a, b):
    return a + b

a = 5
b = 6
summ = addition(a, b)
print(summ)

# Write a function greet that takes a name as an argument
# and prints a greeting. If no name is provided,
# it should default to "Guest".

def greet(name="guest"):
     print("welcome,",name)

greet("rojan")
greet()

# Write a function subtract that takes two keyword
# arguments a and b and returns the result of a - b.

def substract(a, b):
     return a - b

sub = substract(5,6)
print(sub)

# Write a function multiply that takes two arguments:
# a (mandatory) and b (default to 1). Return the result of a * b.

def multi(a,b=1):
     return a*b

mul=multi(5)
print(mul)

# Write a function sum_all that takes any number of 
# positional arguments and returns their sum.

def all_summ(*a):
    return sum(a)

x = all_summ(5,6,7,8,4,5,6,3,5,6,4,34,56,4,3,5,6) 
print(x)