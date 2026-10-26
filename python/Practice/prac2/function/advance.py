# Write a function process_numbers that takes a mandatory
# argument start, a default argument end (default to 100),
# and any number of additional numbers. The function should 
# return the sum of all provided numbers starting from start
# and up to end.

def process_numbers(start, end=100, *args):
    return start + end + sum(args)

result1 = process_numbers(10)
print("Result 1:", result1)  

result2 = process_numbers(10, 20)
print("Result 2:", result2) 

result3 = process_numbers(10, 20, 5, 15, 25)
print("Result 3:", result3)  

result4 = process_numbers(5, *range(11))
print("Result 4:", result4)  

result5 = process_numbers(10, 50, 1, 2, 3, 4, 5)
print("Result 5:", result5)  


# Write a function describe_pet that takes the following arguments:
# name (mandatory positional argument)
# species (default argument, default to "dog")
# Any number of additional characteristics as keyword arguments.
# The function should print a description of the pet.

def describe_pet(name, species="dog", **kwargs):
    print(f"Name: {name}, Species: {species}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_pet("Buddy", age=5, color="brown", breed="Labrador")