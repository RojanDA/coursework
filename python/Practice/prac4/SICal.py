# Build a Python program that calculates simple interest based on user input for principal, rate, and time.

def SIcal(p, t, r):
    return (p * t * r) / 100

def main():
    while True:
        try:
            p = float(input("Enter the principal amount: $"))
            t = float(input("Enter the time in years: "))
            r = float(input("Enter the rate of interest: %"))
            result = SIcal(p, t, r)
            print(f"The simple interest is: ${result:.2f}")
            play_again = input("Do you want to calculate again? (y/n): ").lower
            if play_again == 'n':
                print("Thanks for using the simple interest calculator!")
                break
            elif play_again != 'y':
                print("Invalid input! Exiting the calculator.")
                break
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

main()