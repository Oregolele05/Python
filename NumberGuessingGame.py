import random as rand

lowest = 1
highest = 10
answer = rand.randint(lowest, highest)
guesses = 0
is_running = True

while is_running:
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        if guess > answer:
            print("Too high!")
            guesses += 1

        elif guess < answer:
            print("Too low!")
            guesses += 1

        if guess == answer:
            is_running = False
            print("You got it!")


print(f"The answer was {answer}")
print(f"It took you {guesses} guesses to get it right")