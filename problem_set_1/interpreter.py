expression = input("Expression: ")
component = expression.split(' ')
num1 = component[0]
op = component[1]
num2 = component[2]

if op == "+":
    ans = float(int(num1)+int(num2))
elif op == "-":
    ans = float(int(num1)-int(num2))
elif op == "*":
    ans = float(int(num1)*int(num2))
elif op == "/":
    ans = float(int(num1)/int(num2))
else:
    print("unsupprted operator")

print(f"{ans:.1f}")
