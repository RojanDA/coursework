# Write a program that finds the first number between 1 and 100
# that is divisible by both 7 and 11


for i in range(100):
     if (i+1)%7 == 0 and (i+1)%11 == 0:
          print(i+1)

