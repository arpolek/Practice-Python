import random

number = random.randint(1, 9)
correct = False
i = 0
guess = 0

while correct == False and guess != 'exit':
    guess = input("Guess the number (between 1 and 9) or type 'exit' to stop the game: ")
    if guess == "exit":
        break
    guess = int(guess)
    i = i+1
    if guess < number:
        print("Too low, try again. ")
    elif guess > number:
        print("Too high, try again. ")
    else:
        print("Correct! i = ", i)

