# grettings = input("Greeting: ")
# grettings_mod = grettings.lower().replace(" ",  "")
# if "hello" in grettings_mod:
#     print("$0")
# elif grettings_mod[0] == "h":
#     print("$20")
# else:
#     print("$100")




def main():
    grettings = input("Greeting: ")
    grettings_mod = grettings.lower().replace(" ",  "")
    value(grettings_mod)

def value(greeting):
    if "hello" in greeting:
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()