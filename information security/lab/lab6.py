def gcd(a, b):
    # Ensure that a is the greater number
    if a < b:
        a, b = b, a
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a
 
 
# Example usage
first_number = int(input("Enter the first integer: "))
second_number = int(input("Enter the second integer: "))
 
result = gcd(first_number, second_number)
print(f"The GCD of {first_number} and {second_number} is: {result}")
