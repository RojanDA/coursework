# Write a program to check if a given string is a palindrome


str = input("enter the sring: ")

rstr = str[::-1]

if str == rstr:
    print("palindrome")
else:
    print("not palindrome")