# Write a function print_info that takes any number
# of keyword arguments and prints them in
# the format key: value.

def print_info(**k):
    for key, value in k.items():
        print(f"{key}: {value}")

print_info(key="rojan",value ="tata")

# Write a function power that takes two arguments,
# base and exp, and returns base raised to the power of exp. 
# Then, call this function by unpacking a list of two elements.

def power(base, exp):
    return base ** exp

args = [2, 3]
print(power(*args))

# Write a function display that takes two arguments,
#  name and age, and prints them. Then, call this 
# function by unpacking a dictionary with keys name and age.

def display(name, age):
    print(f"Name: {name}, Age: {age}")

info = {"name": "Alice", "age": 30}
display(**info)
