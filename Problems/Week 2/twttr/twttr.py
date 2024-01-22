# original = input("Input: ")
# result = ""
# vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

# for c in original:
#     if c not in vowels:
#         result +=  c
# print(f"Output: {result}")

def main():
    word = input("Word: ")
    result = shorten(word)
    print(result)

def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    shortened = ""
    for c in word:
        if c not in vowels:
            shortened +=  c
    return shortened

if __name__ == "__main__":
    main()