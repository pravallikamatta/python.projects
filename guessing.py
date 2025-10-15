import random

print("Let me think of a number between 1 and 50...")
num = random.randint(1, 50)

lvl = input("Choose level of difficulty (easy/hard): ").lower()

if lvl == "easy":
    attempts = 10
elif lvl == "hard":
    attempts = 5
else:
    print("Invalid level! Defaulting to easy mode.")
    attempts = 10

print(f"You have {attempts} attempts.")

while attempts > 0:
    guess = int(input("Make a guess: "))

    if guess == num:
        print("🎉 Your guess is right! You win!!")
        break
    elif guess > num:
        print("Too high!")
    else:
        print("Too low!")

    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts left. Guess again!\n")
    else:
        print(f"😞 You've run out of attempts! The correct number was {num}.")