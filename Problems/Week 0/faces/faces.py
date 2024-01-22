def main():
    text = input("Type here: ")
    convert(text)

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    print(text)

main()
