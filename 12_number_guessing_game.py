import random
from number_game import logo

def random_number():
    num = random.randint(1, 100)
    return num

def difficulty_level():
    amount_of_guesses = {'hard': 5, 'easy': 10}
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return amount_of_guesses[difficulty]

def guesses(guesses_left, num):
    while guesses_left != 0:
        print(f"You have {guesses_left} attempts remaining to guess the number")
        guess = int(input('Make a guess: '))
        if guess == num:
            return guess
        else:
            guesses_left -= 1
            if guess > num:
                print('Too high')
            if guess < num:
                print('Too low')
    return guess
    

def game():

    total_guesses = difficulty_level()
    number = random_number()
    guess = guesses(total_guesses, number)
    
    if guess == number:
        print(f"You win! The number was {number}")
    else:
        print(f"You lose! the number was {number}")

print(logo)
print("Welcome to the Guess the Number!\nI am thinking of a number between 1 and 100")
game()