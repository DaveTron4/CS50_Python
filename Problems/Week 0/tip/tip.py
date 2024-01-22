def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = d.replace("$", "")
    dollars = float(dollars)
    print (dollars)
    return dollars


def percent_to_float(p):
    percentage = p.replace("%", "")
    percentage = int(percentage)
    print (percentage / 100)
    return percentage / 100

main()