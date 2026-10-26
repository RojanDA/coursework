# wap to find factorial

def factorial(num):
    if num < 0:
        print("factorial does not exist")
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num- 1)
        

num = int(input("enter a number: "))
fac = factorial(num)
print(fac)