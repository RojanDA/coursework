#Write a program that checks if a number is positive, negative, or zero.
x=1
while x != 0:
 x = int(input("enter any number: "))

 if x < 0:
    print("number is negative")
 elif x > 0:
    print("number is positive") 
 else:
    print("number is zero")  