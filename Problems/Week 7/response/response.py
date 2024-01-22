from validator_collection import checkers

def main():
    print(validate(input("What's your email address? ")))

def validate(email):
    valid_email = checkers.is_email(email)
    if valid_email:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()