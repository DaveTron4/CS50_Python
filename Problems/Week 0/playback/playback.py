main = input("Type something: ")
result = ""
for i in main:
    if i == " ":
        result += "..."
    else:
        result += i
print (result)