# Manual version of Guessing Game
import random

bottom_limit = 0
top_limit = 100
my_rand_int = random.randint(bottom_limit, top_limit)
number_of_guesses = 0 
 
guess = ''
print(f'Welcome to the guessing game! \nGuess a number from {bottom_limit} to {top_limit - 1}')

while guess != my_rand_int: 
  guess = input(f'Please enter your guess: ')

  try:
    guess = int(guess)
  except ValueError:
    print('Please enter a numeric character.')
    break
 
  number_of_guesses = number_of_guesses + 1

  if guess > my_rand_int:   
    print('Your guess was too high.') 
    print(f' Attempt number: {number_of_guesses}')

  elif guess < my_rand_int: 
    print('Your guess was too small.')
    print(f' Attempt number: {number_of_guesses}')
    
  elif guess == my_rand_int:
    if guess == 1:
      try_tries = "try"
    else:
      try_tries = "tries"
    print(f'You win! The number was {my_rand_int}! \nIt took you {number_of_guesses} {try_tries}.')
