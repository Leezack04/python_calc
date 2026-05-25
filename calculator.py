import sys

print("===== Python Calculator =====")

num1 = int(sys.argv[1])
opp = sys.argv[2]
num2 = int(sys.argv[3])

if opp == "+":
    print("Result:", num1 + num2)

elif opp == "-":
    print("Result:", num1 - num2)

elif opp == "*":
    print("Result:", num1 * num2)

elif opp == "/":
    print("Result:", num1 / num2)

else:
    print("Invalid Operator")
