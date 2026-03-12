name = input("Enter your name: ")
print(f"Hello, {name}, Welcome to Ali Raza's Program")

num1 = input("Enter first Number: ")
int(num1)
num2 = input("Enter Second Number: ")
int(num2)
total = float(num1) + float(num2)
print(f"The total is {total}")

# NOW HERE IS THE GUESSING GAME
number = 7
print("Welcome to Number guessing Game")
print("|Number is between 1 and 10")
num = input("Guess the number: ")
int(num)
if int(num) < 7:
  print("Too small! Guess again")
if int(num) > 7:
  print("Too Big! Guess again")
if int(num) == 7:
  print("Congratulatons! You guessed the number. Here is your candy 🍬")