# Create a Python program that converts temperatures between Celsius and Fahrenheit.



def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    while True:
        print('''Select conversion type:
          1. Celsius to Fahrenheit
          2. Fahrenheit to Celsius''')
        choice = input("Enter your choice (1/2): ")
        if choice in ('1', '2'):
            if choice == '1':
                celsius = float(input("Enter temperature in Celsius: "))
                result = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is {result:.2f}°F")
            elif choice == '2':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                result = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is {result:.2f}°C")
            play_again = input("Do you want to convert another temperature? (y/n): ").lower()
            if play_again == 'n':
                print("Thanks for using the temperature converter!")
                break
            elif play_again != 'y':
                print("Invalid input! Exiting the converter.")
                break
        else:
            print("Invalid choice! Please select a valid conversion type.")
            continue

temperature_converter()