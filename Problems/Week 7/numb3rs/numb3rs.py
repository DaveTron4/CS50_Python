import re
import sys


def main():
    valid_ip = validate(input("IPv4 Address: "))
    print(valid_ip)


def validate(ip):
    try:
        valid_ip = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        valid = ""
        if re.match(valid_ip, ip):
            valid = True
        else:
            valid = False
        return valid
    except TypeError:
        sys.exit("Invalid type")


if __name__ == "__main__":
    main()