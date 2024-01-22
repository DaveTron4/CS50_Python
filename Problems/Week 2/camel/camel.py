original = input("camelCase: ")
result = ""

for c in original:
    if c.isupper():
        result += f"_{c.lower()}"
    else:
        result += c
print(f"snake_case: {result}")