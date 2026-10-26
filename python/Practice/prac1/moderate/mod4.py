# Write a program to print numbers from 1 to 20, but skip numbers
# that are multiples of 3 using the continue statement.

for i in range(20):
    if (i+1)%3 == 0 :
        continue
    print(i+1)