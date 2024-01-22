import datetime

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    try:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
            new_date(month, day, year)
        else:
            month, day, year = date.split()
            month_num = months.index(month) + 1
            if "," not in day:
                raise ValueError
            new_date(month_num, day.replace(",", ""), year)
    except ValueError:
        main()

def new_date(month, day, year):
    try:
        d = datetime.datetime(int(year), int(month), int(day))
        if int(month) > 12 or int(day) > 31:
            main()
        print('{:%Y-%m-%d}'.format(d))
    except ValueError:
        main()


main()
