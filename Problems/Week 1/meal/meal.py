def main():
    time = input("What time is it? ")
    converted = convert(time)
    if converted >= 7.0 and converted <= 8.0:
        print("breakfast time")
    elif converted >= 12.0 and converted <= 13.0:
        print("lunch time")
    elif converted >= 18.0 and converted <= 19.0:
        print("dinner time")

def convert(time):
    vals = time.split(':')
    t, hours = divmod(float(vals[0]), 24)
    t, minutes = divmod(float(vals[1]), 60)
    minutes = minutes / 60.0
    return hours + minutes

if __name__ == "__main__":
    main()