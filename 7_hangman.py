import random
from hangman import hangman_images, logo, word_list
import os

os.system('cls')
print(logo)
 
display = []
lives = 6
used_letters = []

#Finds word for the game, then creates the display for the word
chosen_word = random.choice(word_list)
for character in chosen_word:
    display.append('_')

while '_' in display:    
    guess = input('Guess a letter: ').lower()
    os.system('cls')                                                    
    if guess in used_letters:
        print(f'\nYou have already guessed \'{guess}\'. Try again!')
    elif guess.isalpha() == False:
        print('\nYou did not type a letter. Try again!')
    elif len(guess) > 1:
        print('\nYou typed more than 1 letter. Try again!')

    elif guess in chosen_word:
        for n in range(0, len(chosen_word)):
            if guess == chosen_word[n]:
                display[n] = guess
    else:
        print(f"\nThe letter \'{guess}\' is not in the word.")
        lives -= 1

#Creates list of used letters, then displays the unknown word with the corresponding lives left image
    used_letters.append(guess)
    hangman = hangman_images[lives]
    print(f"\n {' '.join(display)}")                     
    print(hangman)
    if lives == 0:
        break

if not '_' in display:
    print(f"\nYou win! The word was \'{chosen_word}\'.")
else:
    print(f"\nYou lose! The word was \'{chosen_word}\'.")
