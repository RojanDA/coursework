# Write a program that repeatedly asks the user for a number
#  until they enter a valid integer

x = 0

while(x!=5):
    x = int(input("enter the value: "))
    if x == 5:
        print("congratulation")
        break
    else:
        print("enter the correct value")