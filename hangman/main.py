#Welcome to Hangman. Please go to vault.py to choose your list of words
from options import secret_word

list_of_guesses = []
wrong_guesses = []

won = False

print("Here is the word:")
print("_ " * len(secret_word))

while (len(wrong_guesses) < 7) and won == False:
    display_word = []
    guess = input("Guess a letter: ")
    # guess_count += 1
    list_of_guesses.append(guess.lower())
    if guess not in secret_word and guess not in wrong_guesses:
      wrong_guesses.append(guess.lower())

    len_counter = 0
    for char in secret_word: 
      if char in list_of_guesses:
        display_word.append(char)
        len_counter += 1
        
        if len_counter == len(secret_word):
          won = True
          print("You won!")
        
      else:
        display_word.append("_")
      
    display_str = ' '.join(display_word)
    print(display_str)
    if won == True:
      break
      
    str_guesses = ', '.join(wrong_guesses)

    if wrong_guesses == []:
      pass
    else:
      print(f'Your wrong guesses so far are: {str_guesses}')

else:
  print("You are out of guesses. The word is", secret_word)
