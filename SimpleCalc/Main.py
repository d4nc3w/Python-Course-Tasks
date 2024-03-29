
operator = input("Enter an operator (+ - * /): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print(f"{operator} is invalid")

print(f"Result: {round(result, 2 )}")