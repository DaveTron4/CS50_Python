import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    result = re.search("https?://(www.)?youtube.com/embed/xvFZjo5PgG0", s)
    if result and re.search("iframe", s):
        return "https://youtu.be/xvFZjo5PgG0"
    else:
        return None


if __name__ == "__main__":
    main()

"http://youtube.com/embed/xvFZjo5PgG0"
"http://youtube.com/embed/xvFZjo5PgG0"