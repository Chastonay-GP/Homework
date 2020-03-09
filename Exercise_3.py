#Exercise 3

import random

from random import randint
randomnum = randint(0,20)
guessesTaken = 0

answers_if_too_high = ["Duh, too high","TOOOOOO HIGH", "YOU HIIIIGH","Very good! ... But too high"]
answers_if_too_low = ["Duh, too low","TOOOOOO low", "Ain't no mountain high enough","Very good! ... But too low"]

print("I am thinking of a number between 1 and 20.")

while guessesTaken < 6:
    print('Take a guess.')
    guess = int(input())

    guessesTaken = guessesTaken + 1

    if guess < randomnum:
        print(random.choice(answers_if_too_low))
    if guess > randomnum:
        print(random.choice(answers_if_too_high))
    if guess == randomnum:
        break

if guess == randomnum:
    guessesTaken = str(guessesTaken)
    print("Good job! You guessed my number in " + guessesTaken + " guesses!")

if guess != randomnum:
    randomnum = str(randomnum)
    print("Nope. The number I was thinking of was " + randomnum + "!")
