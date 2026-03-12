# Number guessing Game using conditions, loops and random

import random

number = random.randint(1,15)
attempts = 0
while True: # It will keep program running until user guesses the right number
    try:
        guess = int(input("Guess the Number:\t"))
        attempts += 1
        if guess > number:
            print("\nToo High! Guess a lower Number. \n")
        elif guess < number:
            print("\nToo Low! Guess a higher Number.\n ")
        elif guess == number: # it will end the loop because the user guesses right number
            print("\nCongratulations! You guessed the Correct Number. Here is your candy 🍬\n")
            print(f"It took you {attempts} to guess the Correct Answer.\n")
            break
    except ValueError: # it will run if the user enter something else instead of number
        print("\nPlease enter a Number.\n")