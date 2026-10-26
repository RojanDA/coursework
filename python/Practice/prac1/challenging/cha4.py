# Create a class BankAccount with methods to deposit,
# withdraw, and check balance, ensuring that the balance
# cannot be directly accessed or modified.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"deposite amount: {amount}. New balance: {self.__balance}")
        else:
            print("deposite amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
             self.__balance -= amount
             print(f"Withdraw amount: {amount}. New balance: {self.__balance}")
            else:
             print("insufficient funds")
        else:
            print("Withdraw amount must be positive")

    def get_balance(self):
        print(f"current balance: {self.__balance}")
        return self.__balance


account = BankAccount(10000)

while 1:
 x = input("d for deposite, w for withdraw, c for check balance and e for exit: ")  
 match x:
   case 'd'|'D':
      d = int(input("enter the amount you want to deposit: "))
      account.deposit(d) 
   case 'w'|'W':
      w = int(input("enter the amount you want to withdraw: "))
      account.withdraw(w) 
   case 'c'|'C':
      account.get_balance()
   case 'e'|'E':
      print("Thank you for visit")
      break
   case _:
       print("valid input")