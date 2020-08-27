# Manual version of Guessing Game
import random

my_rand_int = random.randint(0,100)
number_of_guesses = 0 
top_limit = 101
bottom_limit = 0 
guess = ''
print(f'Welcome to the guessing game! \nGuess a number between {bottom_limit} and {top_limit - 1}')

while guess != my_rand_int: 
  guess = input(f'Please enter your guess: ')

  try:
    guess = int(guess)
  except ValueError:
    print('Please enter a numeric character.')
    break
 
  number_of_guesses = number_of_guesses + 1

  if guess > my_rand_int:   
    top_limit = guess
    print('Your guess was too high.') 
    print(f' Attempt number: {number_of_guesses}')

  elif guess < my_rand_int: 
    bottom_limit = guess
    print('Your guess was too small.')
    print(f' Attempt number: {number_of_guesses}')
    
  elif guess == my_rand_int:
    print(f'You win! The number was {my_rand_int}! \nIt took you {number_of_guesses} tries.')


