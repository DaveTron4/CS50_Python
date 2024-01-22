# def main():
#     fraction = input("Fraction: ")
#     fuel(fraction)

# def fuel(fraction):
#     try:
#         x, y = fraction.split("/")
#         if int(x) > int(y):
#             raise ValueError
#         percent = int(x) / int(y) * 100
#         if percent >= 99:
#             print("F")
#         elif percent <= 1:
#             print("E")
#         else:
#             print(f"{round(percent)}%")
#     except ValueError:
#         main()
#     except ZeroDivisionError:
#         main()


def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    g = gauge(percentage)

def convert(fraction):
    try:
        x, y = fraction.split("/")
        if y == 0:
            raise ZeroDivisionError
        if int(x) > int(y):
            raise ValueError
        percent = int(x) / int(y) * 100
        return round(percent)
    except (ValueError, ZeroDivisionError):
        print("There is an error.")

def gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
