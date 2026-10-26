def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
 
    gcd, x1, y1 = extended_gcd(b, a % b)
 
    x = y1
    y = x1 - (a // b) * y1
 
    return gcd, x, y
 
 
def multiplicative_inverse(a, n):
    gcd, x, y = extended_gcd(a, n)
 
    if gcd != 1:
        return f"The multiplicative inverse does not exist as {a} and {n} are not coprime."
 
    # Ensure the result is positive
    return (x % n + n) % n
 
 
# Example usage
a = int(input("Enter an integer a: "))
n = int(input("Enter the modulus n: "))
 
inverse = multiplicative_inverse(a, n)
 
print(f"The multiplicative inverse of {a} modulo {n} is: {inverse}")
