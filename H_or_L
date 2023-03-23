import os
import random
from hlgame_data import data
from higherlower_art import logo, vs

def show_logo():
    """Clears screen and displays logo"""
    os.system('cls')
    print(logo)

def choice():
    """Returns a random set from the data list"""
    return random.choice(data)

def new_choices(a, b):
    """Creates new choices while preventing choices with equal followers or duplicate choices"""
    c = a
    a = b
    b = random.choice(data)
    while a['follower_count'] == b['follower_count'] or c == b:
        b = random.choice(data)
    return [a, b]

def check_answer(guess, a, b):
    """Checks user guessed correctly upon return"""
    if a['follower_count'] > b['follower_count']:
        return guess == 'A'
    else:
        return guess == 'B'
    
def get_score(a, b):
    """Scores the user over the course of the game"""
    current_score = 0

    while True:
        print(f"A: {a['name']}, {a['description']}, from {a['country']}")
        print(vs)
        print(f"B: {b['name']}, {b['description']}, from {b['country']}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if check_answer(user_guess, a, b) == True:
            current_score += 1
            show_logo()
            print(f"Correct! Current score: {current_score}")
            new_choice = new_choices(a, b)
            a = new_choice[0]
            b = new_choice[1]
        else:
            return current_score

def play():
    show_logo()
    game = input("Welcome! Do you want to play a game of higher/lower? Type 'y' or 'n': ")

    while game == 'y':

        show_logo()
        choice_a = choice()
        choice_b = choice()
        while choice_a['follower_count'] == choice_b['follower_count']:
            choice_b = choice()

        final_score = get_score(choice_a, choice_b)
        show_logo()
        print(f"Wrong! Final score: {final_score}")
        game = input("Do you want to play again? Type 'y' or 'n': ")

    show_logo()
    print('Come back soon!')

play()
