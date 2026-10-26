# Write a program to print the Fibonacci sequence up to the nth term.

def fibo(n):
    sequ = []
    a, b = 0, 1
    for _ in range(n):
        sequ.append(a)
        a, b = b, a + b
    return sequ

n = int(input("enter the number of turms: "))
if n > 0:
    fibo_se = fibo(n)
    print(f"fibonacci sequence up to {n} terms: {fibo_se}")
elif n < 0:
    print("please enter positive interger.")
else:
    print("please enter valid interger.")
