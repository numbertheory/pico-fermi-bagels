"""Pico-Fermi-Bagels game that does not use any strings."""
from __future__ import print_function
import random

# All guesses are compared to the magic number.
MAGIC_NUMBER = int(random.randrange(100, 1000))
WIN = False
GUESS = 1
MAX_GUESSES = 10


def convert_to_list(integer):
    """Convert 3 digits to a list."""
    ones = integer - int(integer/10)*10
    tens = (integer - (int(integer/100)*100) - ones)/10
    hundreds = int(integer/100)
    return [hundreds, tens, ones]


def evaluate_guess(guess):
    """Compare guess to magic number."""
    response = []
    constant = convert_to_list(MAGIC_NUMBER)
    guess_list = convert_to_list(guess)
    for i in range(0, len(guess_list)):
        if guess_list[i] == constant[i]:
            response.append('FERMI')
        elif guess_list[i] in constant:
            response.append('PICO')
    if response == []:
        response = ['BAGELS!']
    return response

while not WIN:
    USER_GUESS = int(raw_input('Guess #{}: '.format(GUESS)))
    if USER_GUESS < 100:
        print('Guess must be a three digit number.')
    elif USER_GUESS > 1000:
        print('Guess must be a three digit number.')
    else:
        REPLY = evaluate_guess(USER_GUESS)
        if REPLY == ['FERMI'] * 3:
            print('You win!')
            WIN = True
        else:
            print(sorted(REPLY))
            GUESS += 1
            if GUESS > MAX_GUESSES:
                print('No more guesses, you lose!')
                print('The number was: {}'.format(MAGIC_NUMBER))
                break
