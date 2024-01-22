import random
import sys

def main():
    level = get_level()
    tries = 3
    questions = 10
    points = 0
    while questions > 0:
        first_num, second_num, correct = generate_integer(level)
        while tries > 0:
            result = question(first_num, second_num)
            if result != correct:
                print("EEE")
                tries -= 1
                continue
            points += 1
            break

        if tries == 0:
            print(f"{first_num} + {second_num} = {correct}")
            tries = 3
        questions -= 1

    print(f"Score: {points}")
    sys.exit(0)


def question(first_num, second_num):
    result = input(f"{first_num} + {second_num} = ")
    try:
        result = int(result)
        return result
    except ValueError:
        return result

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            valid_levels = [1, 2, 3]
            if level not in valid_levels:
                raise ValueError
            return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        first_num = random.randint(0, 9)
        second_num = random.randint(0, 9)
        correct = first_num + second_num
        return first_num, second_num, correct
    if level == 2:
        first_num = random.randint(10, 99)
        second_num = random.randint(10, 99)
        correct = first_num + second_num
        return first_num, second_num, correct
    if level == 3:
        first_num = random.randint(100, 999)
        second_num = random.randint(100, 999)
        correct = first_num + second_num
        return first_num, second_num, correct


if __name__ == "__main__":
    main()