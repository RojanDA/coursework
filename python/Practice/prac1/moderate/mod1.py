#Write a Python program to reverse a string using slicing.

x = input("enter you string: ")

y = x[::-1]

print(y)


#another process using funtion

def rev(s):
    return s[::-1]

rev_st = rev(x)

print("reverse string:", rev_st)