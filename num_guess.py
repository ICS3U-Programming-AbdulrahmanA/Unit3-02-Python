#!/usr/bin/env python3
# Created By: Abdul
# Date: 10/16/2025
# Program to ask the user to guess a number between 0 and 9
import random


def main():
    # Get guess from user
    guess = float(input("Guess a number between 0-9: "))

    # Calculate computers guess
    computer_guess = random.randint(0, 9)

    # Display results
    if guess == computer_guess:
        print("You guessed correctly!")

    # Display wrong message
    if guess != computer_guess:
        print("Wrong! The correct number was", computer_guess)


if __name__ == "__main__":
    main()
