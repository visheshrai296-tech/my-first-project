# Simple Calculator
num1 = float(input("Pehla number daalo: "))
operator = input("Operation (+, -, *, /): ")
num2 = float(input("Dusra number daalo: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    print("Result:", num1 / num2)
else:
    print("Galat operation!")
