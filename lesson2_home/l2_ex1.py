num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
operator = input('Operator (+, -, *, /, %, **, //: ')

if operator == "+":
    print("The result is:", num1 + num2)
elif operator == "-":
    print("The result is:", num1 - num2)
elif operator == "*":
    print("The result is:", num1 * num2)
elif operator == "**":
    print("The result is:", num1 ** num2)
elif operator == "/":
    if num2 != 0:
        print("The result is:", num1 / num2)
    else:
        print("Division by zero!")
elif operator == "%":
    if num2 != 0:
        print("The result is:", num1 % num2)
    else:
        print("Division by zero!")
elif operator == "//":
    if num2 != 0:
        print("The result is:", num1 // num2)
    else:
        print("Division by zero!")

