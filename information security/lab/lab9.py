import random
 
 
# Function to compute power with modulo (modular exponentiation)
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
 
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1  # Divide the exponent by 2
        base = (base * base) % mod
 
    return result
 
 
# Miller-Rabin Primality Test
def is_prime(n, k):
    if n <= 1:
        return False  # Numbers <= 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    if n % 2 == 0:
        return False  # Even numbers > 2 are not prime
 
    # Find d such that n-1 = 2^s * d with d odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1  # Divide d by 2
        s += 1
 
    # Perform k tests
    for _ in range(k):
        a = random.randint(2, n - 2)  # Random base a between 2 and n-2
        x = mod_exp(a, d, n)
 
        if x == 1 or x == n - 1:
            continue
 
        is_composite = True
        for _ in range(1, s):
            x = mod_exp(x, 2, n)
            if x == 1:
                return False  # n is composite
            if x == n - 1:
                is_composite = False
                break
 
        if is_composite:
            return False  # n is composite
 
    return True  # n is likely prime
 
 
# Example usage
n = int(input("Enter an integer to test for primality: "))
 
# Number of bases to test
k = 5  # The more tests, the more accurate the result
 
if is_prime(n, k):
    print(f"{n} is likely a prime number.")
else:
    print(f"{n} is not a prime number.")
