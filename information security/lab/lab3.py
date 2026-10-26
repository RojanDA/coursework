def encrypt_rail_fence(message, num_rails):
    rails = [[] for _ in range(num_rails)]
    rail = 0
    direction = 1
 
    for ch in message:
        rails[rail].append(ch)
        rail += direction
 
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
 
    return ''.join(''.join(r) for r in rails)
 
 
def decrypt_rail_fence(cipher_text, num_rails):
    rails = [[] for _ in range(num_rails)]
    rail_length = [0] * num_rails
    rail = 0
    direction = 1
 
    for _ in cipher_text:
        rail_length[rail] += 1
        rail += direction
 
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
 
    index = 0
    for i in range(num_rails):
        for _ in range(rail_length[i]):
            rails[i].append(cipher_text[index])
            index += 1
 
    rail = 0
    direction = 1
    decrypted_text = ""
 
    for _ in cipher_text:
        decrypted_text += rails[rail].pop(0)
        rail += direction
 
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
 
    return decrypted_text
 
 
# Example usage
num_rails = int(input("Enter the number of rails: "))
message = input("Enter the message: ")
 
encrypted_message = encrypt_rail_fence(message, num_rails)
print("Encrypted Message:", encrypted_message)
 
decrypted_message = decrypt_rail_fence(encrypted_message, num_rails)
print("Decrypted Message:", decrypted_message)
