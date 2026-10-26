def encrypt(text, s):
    result = ""
    # traverse text
    for i in range(len(text)):
        ch = text[i]
        # Encrypt Uppercase letters
        if ch.isupper():
            result += chr((ord(ch) + s - 65) % 26 + 65)
        # Encrypt everything else as lowercase
        else:
            result += chr((ord(ch) + s - 97) % 26 + 97)
    return result
 
# Driver Code
text = "Hello World"
s = 4
print("Text :", text)
print("Shift:", s)
print("Cipher:", encrypt(text, s))

def decrypt(text, s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        ch = text[i]
        # Decrypt Uppercase letters
        if ch.isupper():
            result += chr((ord(ch) - s - 65 + 26) % 26 + 65)
        # Decrypt Lowercase letters
        elif ch.islower():
            result += chr((ord(ch) - s - 97 + 26) % 26 + 97)
        # Non-alphabetic characters
        else:
            result += ch
 
    return result
 
# Driver Code
cipher_text = " LippsrAsvph"
s = 4
print("Cipher:", cipher_text)
print("Shift:", s)
print("Decrypted Text:", decrypt(cipher_text, s))
