# a.	Write a Python function that checks if a given string is a palindrome

def reversal(s):
    revStr = ''
    #reversed revers the given string
    for char in reversed(s):
        revStr += char
    return revStr

def palindrome(str1,str2):
    if str1 == str2:
        print(f"given string: {str1} is palindrome")
    else:
        print(f"given string: {str1} is not palindrome")

str = input("enter the string you want to  check: ")
revStr = reversal(str)
palindrome(str,revStr)


#another process
def palin(s):
    # remove any spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    
    # compare the string with its reverse
    return s == s[::-1]

str = "A man a plan a canal Panama"
if palin(str):
    print(f'"{str}" is a palindrome.')
else:
    print(f'"{str}" is not a palindrome.')