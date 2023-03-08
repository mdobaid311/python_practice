import random
number = random.randint(1, 100)

while (True):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number:
        print("You guessed it right!")
        break
    elif guess > number:
        print("You guessed it wrong! Try a smaller number")
    else:
        print("You guessed it wrong! Try a larger number")
