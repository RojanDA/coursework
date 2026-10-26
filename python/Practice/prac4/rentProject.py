#calculate rent you have to pay in the room
# inputes we need form the user
# total rent
# total food ordered for snacks
# electricity units spend
# charge per unit
# persons in room

# output
# total amount you have to pay

rent = int(input("Enter the total rent: "))
snacks = int(input("Enter the total food ordered for snacks amount: "))
electricity_units = int(input("Enter the electricity units spent: "))
charge_per_unit = int(input("Enter the charge per unit of electricity: "))
persons = int(input("Enter the number of persons in the room: "))
# calculate total electricity charge

def calculate_electricity_charge(units, charge_per_unit):
    return units * charge_per_unit

total_electricity_charge = calculate_electricity_charge(electricity_units, charge_per_unit)


output = (rent + snacks + total_electricity_charge) / persons

print(f"The total amount you have to pay is: {output:.2f}")
