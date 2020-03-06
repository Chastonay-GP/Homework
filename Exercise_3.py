#Exercise 3
from random import randint
randomnum = randint(0,20)
guessesTaken = 0

print("I am thinking of a number between 1 and 20.")

while guessesTaken < 6:
    print('Take a guess.')
    guess = int(input())

    guessesTaken = guessesTaken + 1

    if guess < randomnum:
        print('Your guess is too low.')
    if guess > randomnum:
        print('Your guess is too high.')
    if guess == randomnum:
        break

if guess == randomnum:
    guessesTaken = str(guessesTaken)
    print("Good job! You guessed my number in " + guessesTaken + " guesses!")

if guess != randomnum:
    randomnum = str(randomnum)
    print("Nope. The number I was thinking of was " + randomnum + "!")
