from datetime import date
import sys
import re
import inflect

p = inflect.engine()

def main():
    try:
        birth_date = input("")
        check = re.fullmatch("\d{4}-\d{2}-\d{2}", birth_date)
        if check:
            print(calculate(birth_date))
        else:
            raise ValueError
    except ValueError:
        sys.exit("Invalid Date")

def calculate(birth_date):
    try:
        year, month, day = birth_date.split("-")
        birth_date = date(int(year), int(month), int(day))
    except:
        return sys.exit("Invalid Date")
    total_minutes = (date.today() - birth_date).days * 24 * 60
    num_to_word = p.number_to_words(total_minutes, andword = "").capitalize()
    return num_to_word + " minutes"

if __name__ == "__main__":
    main()