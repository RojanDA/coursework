def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result
 
 
def is_primitive_root(g, p):
    # Check if g is a valid candidate
    if g <= 0 or g >= p:
        return False
 
    seen = []
 
    # Check the powers of g modulo p
    for i in range(1, p):
        value = mod_exp(g, i, p)
        if value in seen:
            return False
        seen.append(value)
 
    # If all values from 1 to p-1 are seen, g is a primitive root
    seen.sort()
    for i in range(1, p):
        if seen[i - 1] != i:
            return False
 
    return True
 
 
# Example usage
p = int(input("Enter a prime number (p): "))
g = int(input(f"Enter a number (g) to check if it's a primitive root of {p}: "))
 
# Validate input
if p <= 1 or g <= 0:
    print("Invalid input. Both inputs must be positive integers, and p must be greater than 1.")
else:
    if is_primitive_root(g, p):
        print(f"{g} is a primitive root of {p}.")
    else:
        print(f"{g} is not a primitive root of {p}.")
