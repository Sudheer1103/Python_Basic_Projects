import random

number = random.randint(1, 100)
count = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        count += 1

        if guess == number:
            print(f"You guessed correctly in {count} guesses!")
            break
        elif guess < number:
            print("Try a bigger number.")
        elif guess > number:
            print("Try a smaller number.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
