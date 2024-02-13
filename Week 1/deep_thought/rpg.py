import random

num1 = random.randint(0,12)
num2 = random.randint(0,12)

multiply = num1 * num2

guesses = 0


while guesses < 10:
    guess = input(f'Whats {num1} times {num2} ?')
    guess = int(guess)
    if guess == multiply:
        print('Correct')