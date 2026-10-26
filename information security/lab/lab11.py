def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result
 
 
# Generate a large prime number (p) and a primitive root (g) for the demonstration
p = 23  # In real applications, use much larger prime numbers
g = 5   # In real applications, select a generator carefully
 
print(f"Public parameters: p = {p}, g = {g}")
 
# Alice's private key (a) and public key (A)
a = 6  # Alice's private key
A = mod_exp(g, a, p)  # Alice's public key
print(f"Alice's private key: a = {a}")
print(f"Alice's public key: A = {A}")
 
# Bob's private key (b) and public key (B)
b = 15  # Bob's private key
B = mod_exp(g, b, p)  # Bob's public key
print(f"Bob's private key: b = {b}")
print(f"Bob's public key: B = {B}")
 
# Exchange public keys and compute the shared secret
# Alice computes the shared secret s using Bob's public key B and her private key a
shared_secret_alice = mod_exp(B, a, p)
print(f"Shared secret computed by Alice: {shared_secret_alice}")
# Bob computes the shared secret s using Alice's public key A and his private key b
shared_secret_bob = mod_exp(A, b, p)
print(f"Shared secret computed by Bob: {shared_secret_bob}")
# Both should be the same
if shared_secret_alice == shared_secret_bob:
    print(f"Key exchange successful. Shared secret: {shared_secret_alice}")
else:
    print("Key exchange failed. Shared secrets do not match.")