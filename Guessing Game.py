# this is a number guessing game
import random

guessesTaken = 0
print('Hello! What is your name?  ')
myName = input()
number = random.randint(1, 200)
print('Well, ' + myName + ' I am thinking of a number between 1 and 200')

while guessesTaken < 20:
    print('Take a guess')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is to low')

    if guess > number:
        print('Your guess is to high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good Job ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. the number i was thinking of was ' + number)
