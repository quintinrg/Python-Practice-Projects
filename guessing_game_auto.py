# Automatic version of Guessing Game
import random
import time

my_rand_int = random.randint(0,100)
number_of_guesses = 0 
top_limit = 101
bottom_limit = 0 
guess = ''
print(f'Welcome to the guessing game! \nThe machine will guess a number between {bottom_limit} and {top_limit - 1}')

while guess != my_rand_int: 
  time.sleep(0.5)
  guess = (bottom_limit + top_limit) / 2
  guess = int(guess)
  print(f'Guessing {guess}')
  number_of_guesses = number_of_guesses + 1

  if guess > my_rand_int:   
    top_limit = guess
    print('Guess was too high.') 
    print(f' Attempt number: {number_of_guesses}')

  elif guess < my_rand_int: 
    bottom_limit = guess
    print('Guess was too small.')
    print(f' Attempt number: {number_of_guesses}')
    
  elif guess == my_rand_int:
    print(f'Correct number found! It was {my_rand_int}! \nIt took {number_of_guesses} tries.')


