def create_state_array(user_input):
    state = [[0] * 4 for _ in range(4)]
    user_input = user_input.ljust(16, '\0')[:16]  # Pad/trim input to 16 bytes
    for i in range(16):
        state[i % 4][i // 4] = ord(user_input[i])
    return state
 
 
def print_state_array(state):
    for row in range(4):
        for col in range(4):
            print(f"{state[row][col]:02X}", end=" ")
        print()
 
 
# Example usage
user_input = input("Enter a message (up to 16 characters): ")
 
state_array = create_state_array(user_input)
print("4x4 State Array:")
print_state_array(state_array)
