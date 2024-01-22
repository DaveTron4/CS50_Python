menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}



def main():
    try:
        item = input("Item: ").title()
        order(item)
    except EOFError:
        print("")

total = 0.00

def order(item):
    global total
    try:
        if item in menu:
            total = total + menu[item]
            print(f"Total: ${total:.2f}")
            main()
        else:
            main()
    except KeyError:
        pass



main()