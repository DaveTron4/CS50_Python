import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    scourgify = Scourgify(sys.argv[1], sys.argv[2])
    scourgify.scourgify_read()
    scourgify.scourgify_write()
    sys.exit(0)

class Scourgify:
    def __init__(self, file1, file2):
        self.file1 = file1
        self. file2 = file2
        self.data = []

    def scourgify_read(self):
        try:
            with open(self.file1, newline = '') as cvsfile:
                reader = csv.DictReader(cvsfile)
                for row in reader:
                    self.data.append({'name': row['name'], 'house': row['house']})
        except FileNotFoundError:
            sys.exit(f"Coult not read {self.file1}")

    def scourgify_write(self):
        try:
            with open(self.file2, 'w', newline = '') as csvfile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
                writer.writeheader()
                for entry in self.data:
                    last_name, first_name = entry['name'].split()
                    house = entry['house']
                    writer.writerow({'first': first_name.strip(","), 'last': last_name.strip(","), 'house': house})
        except ValueError:
            sys.exit("sum happend")

if __name__ == "__main__":
    main()