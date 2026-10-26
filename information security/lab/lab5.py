# Permutation Choice 1 (PC-1) table
pc1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]
 
# Permutation Choice 2 (PC-2) table
pc2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]
 
# Number of rotations per round
num_rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
 
 
# Function to permute bits according to a given table
def permute(input_bits, table):
    return ''.join(input_bits[i - 1] for i in table)
 
 
# Function to left-rotate a binary string
def rotate_left(input_bits, num_bits):
    return input_bits[num_bits:] + input_bits[:num_bits]
 
 
# Function to generate 16 subkeys
def generate_subkeys(key):
    # Initial permutation using PC-1
    key = permute(key, pc1)
 
    # Split into two 28-bit halves
    left = key[:28]
    right = key[28:56]
 
    subkeys = []
 
    # Generate 16 subkeys
    for round_num in range(16):
        # Rotate halves
        left = rotate_left(left, num_rotations[round_num])
        right = rotate_left(right, num_rotations[round_num])
 
        # Combine halves and permute using PC-2 to get the subkey
        combined = left + right
        subkeys.append(permute(combined, pc2))
 
    return subkeys
 
 
# Example usage
key = input("Enter a 64-bit binary key: ").strip()
 
# Validate key length
if len(key) != 64:
    print("Invalid key length. Please enter a 64-bit binary key.")
else:
    subkeys = generate_subkeys(key)
 
    print("Generated Subkeys:")
    for i in range(16):
        print(f"K{i + 1:02d}: {subkeys[i]}")
