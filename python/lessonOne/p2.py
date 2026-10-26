# wap to swap two variable

def swap(a,b):
    temp = a
    a = b
    b = temp
    print(f'a = {a} and b = {b}')

a = int(input("enter 1st number: "))
b = int(input("enter 2st number: "))
print(f'a = {a} and b = {b}')
print("after swap:")
swap(a,b)



      
     