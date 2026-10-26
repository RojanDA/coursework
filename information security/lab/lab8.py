import random
 
 
# Function to compute power with modulo
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
 
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1  # Divide the exponent by 2
        base = (base * base) % mod
 
    return result
 
 
# Function to test primality using Fermat's Little Theorem
def is_prime(p, k):
    if p <= 1:
        return False  # Numbers <= 1 are not prime
    if p <= 3:
        return True  # 2 and 3 are prime numbers
 
    # Test k different values of a
    for _ in range(k):
        a = random.randint(2, p - 2)  # Random base a between 2 and p-2
        if mod_exp(a, p - 1, p) != 1:
            return False
 
    return True
 
 
# Example usage
p = int(input("Enter an integer to test for primality: "))
 
# Number of bases to test
k = 5  # The more tests, the more accurate the result
 
if is_prime(p, k):
    print(f"{p} is likely a prime number.")
else:
    print(f"{p} is not a prime number.")
