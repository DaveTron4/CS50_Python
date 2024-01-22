expression = input("Expression: ")
x, y, z = expression.split(" ")
expressions = ["+", "-", "/", "*"]
result = ""
for expression in expressions:
    if y == "+":
        result = int(x) + int(z)
    elif y == "-":
        result = int(x) - int(z)
    elif y == "/":
        result = int(x) / int(z)
    elif y == "*":
        result = int(x) * int(z)
print(float(result))