# A dice simulator
import random

def roll_dice():
    result = random.randint(1,6)
    print(f"🎲 You rolled a {result}")


roll_dice() 