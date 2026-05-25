# calculator.py

# calculator.py

print("===== Python Calculator =====")

# Get user input
num1 = 
operator = input("Enter operator (+, -, *, /): ")
num2 = 
# Perform calculation
if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid operator")
