import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    print(count_lines(sys.argv[1]))


def count_lines(file):
    try:
        count = 0
        with open(file, "r") as f:
            for l in f:
                if not (l.lstrip().startswith("#") or l.strip() == ""):
                    count += 1
            return count
    except FileNotFoundError:
        sys.exit("File does not Exist")


if __name__ == "__main__":
    main()