#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program uses a try statement

import random


def main():
    # this function uses a try statement

    print("")
    print("This program makes the user guess the number that"
          "the computer has saved.")
    guess_str = input("Please input a number (from 0 to 9): ")
    print("")
    generated_number = random.randint(0, 9)
    generated_number_str = str(generated_number)
    try:
        guess = int(guess_str)
        print("You entered an integer correctly")
        print("")
    except Exception:
        print("This was not an integer")
    else:
        if generated_number == guess:
            print("You Guessed Correctly! Yay! Please Play Again")
        else:
            print("You guessed incorrectly :( Please Try Again")
            print("The correct number was " + generated_number_str)


if __name__ == "__main__":
    main()
