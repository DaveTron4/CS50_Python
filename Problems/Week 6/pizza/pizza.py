from tabulate import tabulate
import csv
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    print(reader(sys.argv[1]))


def reader(file_name):
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            headers = next(reader)
            table = [row for row in reader]
        table = tabulate(table, headers, tablefmt = "grid")
        print(table)
        sys.exit()
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()