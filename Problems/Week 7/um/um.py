import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    pattern = re.compile(r"\bum\b", re.IGNORECASE)
    count = len(re.findall(pattern, s))
    return count

if __name__ == "__main__":
    main()