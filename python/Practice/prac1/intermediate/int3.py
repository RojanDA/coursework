#  Write a program to print a multiplication table for numbers from 1 to 5.

s=1
while s <= 5:
    for i in range(1,11):
        print(s,"X",i,"=",s * i)
    s +=1