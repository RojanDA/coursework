# Write a Python program to find the longest substring
# without repeating characters in a given string.

def longest_unique_substring(s):
    start = 0  # Starting index of the current substring
    max_length = 0  # Length of the longest substring found
    max_substr = ""  # Longest substring without repeating characters
    char_index_map = {}  # Dictionary to track the last seen index of each character

    for i, char in enumerate(s):  #The enumerate function is used to iterate over the string s while keeping track of both the index and the character at that index
        # If the character is already in the map and its last seen index is within the current substring
        if char in char_index_map and char_index_map[char] >= start:
            # Move the start index to the right of the last occurrence of the current character
            start = char_index_map[char] + 1
        
        # Update the last seen index of the current character
        char_index_map[char] = i
        
        # Calculate the length of the current substring
        current_length = i - start + 1
        
        # If the current substring is longer than the previously found longest substring
        if current_length > max_length:
            max_length = current_length  # Update the max length
            max_substr = s[start:i+1]  # Update the longest substring

    return max_substr  # Return the longest substring without repeating characters

# Example usage
input_string = input("Enter a string: ")
result = longest_unique_substring(input_string)
print(f"The longest substring without repeating characters is: '{result}'")
