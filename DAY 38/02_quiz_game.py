# A Quiz Game

import random

number = random.randint(1,10)

guess = int(input("Enter a Number: "))

while True:
        try:
         if guess < number:
           print("Too low! Guess a higher Number. ")
         elif guess > number:
            print("Too High! Guess a lower Number. ")
         else:
           print("Congrautlations! You guessed the Correct Numbe. ")
           break
        except Exception as e:
             print(f"An error occured: {e}")
             break