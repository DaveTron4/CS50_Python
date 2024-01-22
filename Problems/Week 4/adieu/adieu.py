import inflect

p = inflect.engine()

names = []

def main():
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            adieu()
            break

def adieu():
    list_of_names = p.join(names)
    print(f"Adieu, adieu, to {list_of_names}")

main()