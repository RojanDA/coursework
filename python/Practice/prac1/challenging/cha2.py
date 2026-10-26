# Write a program that determines the grade (A, B, C, D, F) 
# based on a score input by the user.


score = float(input("enter a score of the studenyt: "))

if score > 0 and score<=100:
    if score >= 90 :
        print("A")
    elif score >= 80 :
        print("B")
    elif score >= 70 :
        print("C")
    elif score >= 60 :
        print("D")
    elif score >= 50 :
        print("E")
    else:
        print("f")
else:
    print("enter score between 1 to 100")
    
