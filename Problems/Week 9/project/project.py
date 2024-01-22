# Final Project name: pyO'clock
# Name: David Salas Carrascal
# City: Lawrenceville
# Country: United States


import pygame
import re
from datetime import datetime
import random
import operator
import os
import sys


def main(input_fn=input):
    date = input_fn("What date do you want the alarm to go off? (in YYYY-MM-DD, leave empty for today): ")
    time_s = input_fn("What time do you want the alarm to go off? (in HH:MM AM/PM): ")
    sound = input_fn("Enter sound of alarm: ")
    name = input_fn("What's the name of the alarm? ")
    set_alarm(date, time_s, sound, name)


def set_alarm(date, time_s, sound, name):
    try:
        pygame.mixer.init()

        if date and not re.match(r"\d{4}-\d{2}-\d{2}", date):
            raise ValueError("Invalid date format")

        if not re.match(r"\d{1,2}:\d{2} [AP]M", time_s):
            raise ValueError("Invalid time format")

        if not os.path.exists(sound):
            raise FileNotFoundError(f"Sound file '{sound}' not found")

        if "AM" in time_s or "PM" in time_s:
            time_s = convert(time_s)

        if date:
            alarm_date_time = datetime.strptime(date + " " + time_s, "%Y-%m-%d %H:%M")
        else:
            alarm_date_time = datetime.strptime(
                datetime.now().strftime("%Y-%m-%d") + " " + time_s, "%Y-%m-%d %H:%M"
            )

        current_time = datetime.now()

        if alarm_date_time < current_time:
            print("Time has to be greater than the current time")
            main()

        time_difference = (alarm_date_time - current_time).seconds
        print(f"Alarm set for {time_s}.")

        pygame.time.delay(time_difference * 1000)
        # winsound.PlaySound(sound,winsound.SND_ASYNC)
        print(f"{name} iS GOING OFF, QUICKLY SOLVE THE PROBLEM TO MAKE IT STOOOPPP!!!")

        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(-1)

        while True:
            answer = questions()
            if answer == True:
                pygame.mixer.music.stop()
                break

        while True:
            new_alarm_question = input("Do you want to set up another alarm? ").upper()
            if new_alarm_question == "YES":
                main()
                break
            elif new_alarm_question == "NO":
                sys.exit()
            else:
                print("It has to be YES or NO.")

    except ValueError as ve:
        print(f"Error: {ve}")
        raise SystemExit
    except pygame.error:
        print("Error initializing pygame")
    except FileNotFoundError as fe:
        print(f"Error: {fe}")


def convert(s):
    try:
        result = ""
        time = re.match(r"\b(?P<time_parts>\d{1,2}:\d{2}) (?P<meridiem>[AP][M])\b", s)
        if time == None:
            raise ValueError
        time_parts = time.group("time_parts").split(":")
        meridiem = time.group("meridiem")
        if int(time_parts[1]) >= 60 or int(time_parts[0]) > 12:
            raise ValueError
        if meridiem == "AM":
            if time_parts[0] == "12":
                time_parts[0] = "00"
                result = f"{time_parts[0].rjust(2, '0')}:{time_parts[1]}"
            else:
                result = f"{time_parts[0].rjust(2, '0')}:{time_parts[1]}"
        elif meridiem == "PM":
            if time_parts[0] == "12":
                result = f"{time_parts[0].rjust(2, '0')}:{time_parts[1]}"
            else:
                first_time_fixed = str(int(time_parts[0]) + 12)
                result = f"{first_time_fixed.rjust(2, '0')}:{time_parts[1]}"
        return result
    except ValueError:
        print("Invalid time format")
        main()


def questions():
    operators = ["+", "-", "*", "/"]
    operator_functions = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator_picked = random.choice(operators)

    print(f"solve to stop alarm: {num1} {operator_picked} {num2}")
    answer_expected = round(operator_functions[operator_picked](num1, num2), 1)

    while True:
        answer = input("Answer: ")
        is_digit = is_number_string(answer)
        if is_digit == True:
            break

    if float(answer) == answer_expected:
        return True
    else:
        return False

def is_number_string(s):
    return bool(re.match(r"^-?\d+(\.\d+)?$", s))

if __name__ == "__main__":
    main()
