def generate_playfair_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    used_chars = set()
    keyword = keyword.upper()
    for ch in keyword:
        if ch not in used_chars and ch in alphabet:
            matrix.append(ch)
            used_chars.add(ch)
    for ch in alphabet:
        if ch not in used_chars:
            matrix.append(ch)
            used_chars.add(ch)
    # Reshape the list into a 5x5 matrix
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]
 
 
def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join(ch for ch in text if ch.isalpha())
    digraphs = []
    i = 0
    while i < len(text):
        digraph = text[i]
        if i + 1 < len(text) and text[i] != text[i + 1]:
            digraph += text[i + 1]
            i += 2
        else:
            digraph += 'X'
            i += 1
        digraphs.append(digraph)
    return digraphs
 
 
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None
 
 
def encrypt_digraph(matrix, digraph):
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])
 
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]
 
 
def decrypt_digraph(matrix, digraph):
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])
 
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]
 
 
def encrypt_message(keyword, message):
    matrix = generate_playfair_matrix(keyword)
    digraphs = preprocess_text(message)
    encrypted_message = ''.join(encrypt_digraph(matrix, d) for d in digraphs)
    return matrix, encrypted_message
 
 
def decrypt_message(keyword, encrypted_message):
    matrix = generate_playfair_matrix(keyword)
    digraphs = preprocess_text(encrypted_message)
    decrypted_message = ''.join(decrypt_digraph(matrix, d) for d in digraphs)
    return decrypted_message
 
 
def display_matrix(matrix):
    for row in matrix:
        print(' '.join(row))
 
 
# Example usage
keyword = "keyword"
message = "hello World"
matrix, encrypted_message = encrypt_message(keyword, message)
print("Playfair Matrix:")
display_matrix(matrix)
 
print("\nEncrypted Message:", encrypted_message)
 
decrypted_message = decrypt_message(keyword, encrypted_message)
print("Decrypted Message:", decrypted_message)
