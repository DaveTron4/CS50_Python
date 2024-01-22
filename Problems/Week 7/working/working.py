import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        result = ""
        if ":" in s:
            time = re.match(r"\b(?P<first_time>\d{1,2}:\d{2}) (?P<first_half>[AP][M]) to (?P<second_time>\d{1,2}:\d{2}) (?P<second_half>[AP][M])\b", s)
            if time == None:
                raise ValueError
            first_time = time.group("first_time").split(":")
            second_time = time.group("second_time").split(":")
            first_half = time.group("first_half")
            second_half = time.group("second_half")
            if int(first_time[1]) >= 60 or int(second_time[1]) >= 60 or int(first_time[0]) > 12 or int(second_time[0]) > 12:
                raise ValueError
            if first_half == "AM" and second_half == "PM":
                if first_time[0] == "12":
                    second_time_fixed = str(int(second_time[0]) + 12)
                    first_time[0] = "00"
                    result = f"{first_time[0].rjust(2, '0')}:{first_time[1]} to {second_time_fixed.rjust(2, '0')}:{second_time[1]}"
                if second_time[0] == "12":
                    result = f"{first_time[0].rjust(2, '0')}:{first_time[1]} to {second_time[0].rjust(2, '0')}:{second_time[1]}"
                else:
                    second_time_fixed = str(int(second_time[0]) + 12)
                    result = f"{first_time[0].rjust(2, '0')}:{first_time[1]} to {second_time_fixed.rjust(2, '0')}:{second_time[1]}"
            elif first_half == "PM" and second_half == "AM":
                if first_time[0] == "12":
                    result = f"{first_time[0].rjust(2, '0')}:{first_time[1]} to {second_time[0].rjust(2, '0')}:{second_time[1]}"
                if second_time[0] == "12":
                    first_time_fixed = str(int(first_time[0]) + 12)
                    second_time[0] == "00"
                    result = f"{first_time_fixed.rjust(2, '0')}:{first_time[1]} to {second_time[0].rjust(2, '0')}:{second_time[1]}"
                else:
                    first_time_fixed = str(int(first_time[0]) + 12)
                    result = f"{first_time_fixed.rjust(2, '0')}:{first_time[1]} to {second_time[0].rjust(2, '0')}:{second_time[1]}"


        else:
            time = re.match(r"\b(?P<first_time>\d{1,2}) (?P<first_half>[AP][M]) to (?P<second_time>\d{1,2}) (?P<second_half>[AP][M])\b", s)
            if time == None:
                raise ValueError
            first_time = time.group("first_time")
            second_time = time.group("second_time")
            first_half = time.group("first_half")
            second_half = time.group("second_half")
            if int(first_time) > 12 or int(second_time) > 12:
                raise ValueError
            if first_half == "AM" and second_half == "PM":
                if first_time == "12":
                    second_time_fixed = str(int(second_time) + 12)
                    first_time = "00"
                    result = f"{first_time.rjust(2, '0')}:00 to {second_time_fixed.rjust(2, '0')}:00"
                if second_time == "12":
                    result = f"{first_time.rjust(2, '0')}:00 to {second_time.rjust(2, '0')}:00"
                else:
                    second_time_fixed = str(int(second_time) + 12)
                    result = f"{first_time.rjust(2, '0')}:00 to {second_time_fixed.rjust(2, '0')}:00"
            elif first_half == "PM" and second_half == "AM":
                if first_time == "12":
                    result = f"{first_time.rjust(2, '0')}:00 to {second_time.rjust(2, '0')}:00"
                if second_time == "12":
                    first_time_fixed = str(int(first_time) + 12)
                    second_time == "00"
                    result = f"{first_time_fixed.rjust(2, '0')}:00 to {second_time.rjust(2, '0')}:00"
                else:
                    first_time_fixed = str(int(first_time) + 12)
                    result = f"{first_time_fixed.rjust(2, '0')}:00 to {second_time.rjust(2, '0')}:00"
        return result

    except ValueError:
        sys.exit("ValueError")


if __name__ == "__main__":
    main()