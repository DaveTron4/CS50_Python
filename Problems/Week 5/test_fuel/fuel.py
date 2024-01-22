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
import sys

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    g = gauge(percentage)

def convert(fraction):
    try:
        x, y = fraction.split("/")
        if int(y) == 0:
            raise ZeroDivisionError
        elif int(x) > int(y):
            raise ValueError
        percent = int(x) / int(y) * 100
        return round(percent)
    except ValueError:
        raise ValueError("Invalid input")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cant divide by zero")

def gauge(percentage):
    if percentage <= 1:
        print("E")
        return "E"
    elif percentage >= 99:
        print("E")
        return "F"
    else:
        percent = f"{percentage}%"
        print(percent)
        return percent


if __name__ == "__main__":
    main()
