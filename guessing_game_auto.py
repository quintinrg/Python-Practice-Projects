# Automated version of Guessing Game

import time
import random

my_rand_int = random.randint(0,100)

number_of_guesses = 0 

top_limit = 101
bottom_limit = 0 

guess = ""

while guess != my_rand_int:
  guess = (top_limit + bottom_limit) / 2 
  
  guess = int(guess)
  
  print(f'Guessing {guess}')

  time.sleep(0.5) 

  number_of_guesses = number_of_guesses + 1

  if guess > my_rand_int: 
    
    top_limit = guess
    print("Your guess was too high") 
    print(f' Attempt number: {number_of_guesses}')

  elif guess < my_rand_int:
   
    bottom_limit = guess
    print("Your guess was too small")
    print(f' Attempt number: {number_of_guesses}')
    
  elif guess == my_rand_int: 

    print(f'You win! The number was {my_rand_int}')
    
    print(f' It took you: {number_of_guesses} tries!')
  
print("The program is complete.") 

