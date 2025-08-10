from art import logo
from random import randint

def random_number():
    return randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def set_diff():
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if diff.lower() == "easy":
        attempts = 10
        print("You have 10 attempts remaining to guess the number.")
    elif diff.lower() == "hard":
        attempts = 5
        print("You have 5 attempts remaining to guess the number.")
    else:
        print("Invalid answer.")
    return attempts

def check_guess(number, attempts):
    game_over = False
    guess = 0
    while not game_over:
        if attempts > 0:
            guess = int(input("Make a guess: "))
            if guess == number:
                print(f"You got it! The answer is {number}.")
                break
            elif guess > number:
                print("Too high.\nGuess again.")
                attempts -= 1
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif guess < number:
                print("Too low.\nGuess again.")
                attempts -= 1
                print(f"You have {attempts} attempts remaining to guess the number.")
            else:
                game_over = True

attempts = set_diff()
number = random_number()
check_guess(number, attempts)
