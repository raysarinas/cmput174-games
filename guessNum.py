# This is the Guess The Number Game

import random 
number = random.randint(1,10)

# The game starts

print('I am thinking of a number between 1 and 10')
guess = input('What is the number? ')
number = str(number)
guess = str(guess)
print ('The number was ' + number)
print ('You guessed ' + guess)  