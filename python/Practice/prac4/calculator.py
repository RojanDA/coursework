# # Create a simple command-line calculator that performs basic arithmetic operations between two numbers.

# Taking user input (numbers and operator
# Using conditional statements (if, elif, else) to decide which operation to perform
# Writing functions for each operation
# Displaying output in a clean way
# Handling division by zero and invalid input

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in ('1','2','3','4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
        else:
            print("Invalid choice! Please select a valid operation.")
            continue
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "n":
            print("Thanks for using the calculator!")
            break
        elif play_again != "y":
            print("Invalid input! Exiting the calculator.")
            break

calculator()
