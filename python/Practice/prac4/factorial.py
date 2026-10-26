# Create a Python program that takes a positive integer as input and returns its factorial.

def factorial(n):
    if n < 0:
        return "error negative number not allowed"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
def main():
    while True:
        num = int(input("Enter a positive integer: "))
        result = factorial(num)
        print(f"The factorial of {num} is: {result}")
        print("Do you want to calculate another factorial? (y/n)")
        play_again = input().lower()
        if play_again == 'n':
            print("Thanks for using the factorial calculator!")
            break
        elif play_again != 'y':
            print("Invalid input! Exiting the calculator.")
            break


main()