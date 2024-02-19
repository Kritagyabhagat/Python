# How to build simple calculator in python
print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
...''')
Num1 = int(input("Enter the value1 :-"))
Num2 = int(input("Enter the value2 :-"))
opr = input("Enter the opr..")
if opr == "+":
    print(Num1+Num2)
elif opr == "-":
    print(Num1-Num2)
elif opr == "*":
    print(Num1*Num2)
elif opr == "/":
    print(Num1/Num2)
else:
    print("Invalid opr....")

num1 = int(input("Enter the value1:-"))
num2 = int(input("Enter the value2:-"))
opr = input("Enter the opr..")
if opr == "+":
    print(num1+num2)
elif opr == "-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
else:
    print("Invalid opr....")