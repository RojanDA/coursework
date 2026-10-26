def euler_totient(n):
    if n == 1:
        return 1
 
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
 
    return result
 
 
# Example usage
n = int(input("Enter an integer to find its Euler's Totient Function: "))
 
print(f"Euler's Totient Function of {n} is: {euler_totient(n)}")
