import random
import sys

def main():
    try:
        level = input("Level: ")
        game(level)
    except ValueError:
        main()

def game(level):
    secret_num = random.randint(1, int(level))
    guess(secret_num)

def guess(secret_num):
    try:
        guess_num = input("Guess: ")
        if int(guess_num) < secret_num:
            print("Too small!")
            guess(secret_num)
        elif int(guess_num) > secret_num:
            print("Too large!")
            guess(secret_num)
        else:
            print("Just right!")
            sys.exit()
    except ValueError:
        guess(secret_num)

main()