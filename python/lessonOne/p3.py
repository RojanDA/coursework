# wap to perform all arithmetic operation on two numbers(addd,subtract,multiply,divide,moduls)

def addition(a,b):
    sum = a + b
    print(sum)
def subtraction(a,b):
    sub = a - b
    print(sub)
def multiplication(a,b):
    mul = a * b
    print(mul)
def divition(a,b):
    if b != 0:  
        div = a / b
        print(div)
    else:
        print("divisible number cannot be zero")

a = int(input("1st number: "))
b = int(input("2nd number: "))
operation = int(input("enter 1 for additin, 2 f or subtraction, 3 for multiplication, 4 for divition: ")) 
match operation:
    case 1:
        addition(a,b)
    case 2:
        subtraction(a,b)
    case 3:
        multiplication(a,b)
    case 4:
        divition(a,b)
    case _:
        print("invalid number")
    

