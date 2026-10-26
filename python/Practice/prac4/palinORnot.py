# Build a Python program that checks whether a word or sentence is a palindrome — a string that reads the same forwards and backwards.
import re
def reverse(s):
    s = s.lower().replace(" ", "")
    ss = re.sub(r'[^a-z]', '', s) 
    return ss == ss[::-1]

def main():
    user_input = input("Enter a word or sentence: ")
    if reverse(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

main()