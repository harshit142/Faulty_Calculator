# Faulty Calculator
#Design a calculator which will correctly solve all the problems except the following ones:-
# 45*3=555, 56+9=77, 56/6=4
#This program will take operator and then two numbers as input from the user and then return the result

x = input("Enter the operator'*,+,/,-' :- ")
y = int(input("Please enter no.1= "))
z = int(input("Please enter no.2= "))

if (x == "*"):
    if (x == "*" and y == 45 and z == 3):
        print(555)
    else:
        print(y*z)
elif (x == "+"):
    if (x == "+" and y == 56 and z == 9):
        print(77)
    else:
        print(y+z)
elif (x == "/"):
    if (x == "/" and y == 56 and z == 6):
        print(4)
    else:
        print(y/z)
elif (x == "-"):
    print(y-z)
