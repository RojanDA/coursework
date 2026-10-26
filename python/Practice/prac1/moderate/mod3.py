# Write a Python program that uses the match-case statement to print
#  the day of the week based on a number input 
# (1 for Monday, 2 for Tuesday, etc.).

x = int(input("enter a number from 1 to 7 to find a day:"))

match x:
    case 1:
        print("monday")
    case 2:
        print("tue")
    case 3:
        print("wed")
    case 4:
        print("thu")
    case 5:
        print("fri")
    case 6:
        print("sat")
    case 7:
        print("sun")
    case _:
        print("invalid input")
 