# Create a Python program that calculates a person’s BMI (Body Mass Index) and categorizes it (e.g., underweight, normal, overweight, obese).

def calculate_bmi(weight, height):
    if height <= 0:
        return "Error: Height must be greater than zero."
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    
def main():
    while True:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        result = categorize_bmi(bmi)
        print(f"Your BMI is: {bmi:.2f} - Category: {result}")
        play_again = input("Do you want to calculate another BMI? (y/n): ").lower()
        if play_again == 'n':   
            print("Thanks for using the BMI calculator!")
            break   
        elif play_again != 'y':
            print("Invalid input! Exiting the calculator.")
            break

main()