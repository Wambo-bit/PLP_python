num1=float(input("enter first number:"))
num2=float(input("enter second number:"))

Operation=input("enter operation (+, -, *, /):")
if Operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif Operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif Operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")    

elif Operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation. Please enter one of +, -, *, /.")