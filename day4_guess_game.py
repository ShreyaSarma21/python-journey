import random #So, the game is not hardcoded to a particular no 

secret_num = random.randint(1, 10)  # Random number between 1 and 10
attempts = 5

print("Welcome to the Guessing Game!")
print("You have 5 attempts to guess the number between 1 and 10.\n")

for attempt in range(attempts):
    try:
        guess = int(input(f"Attempt {attempt + 1} of {attempts} - Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.\n")
        continue  # Skip this round and don't count it as a valid attempt

    if guess == secret_num:
        print("You win!")
        break
    elif guess < secret_num:
        print("Too low! Try a higher number.\n")
    else:
        print("Too high! Try a lower number.\n")
else:
    print(f"Out of attempts! The correct number was {secret_num}. Better luck next time!")

