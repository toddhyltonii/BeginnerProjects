import random
import os
from blackjack import logo

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Deals 2 random cards. If both cards are 11 (aces), reduces one of them
def deal_cards():
    cards = random.choices(deck, k=2)
    if sum(cards) > 21:
        cards = reduce_ace(cards)
        return cards
    else:
        return cards

#Reducs the value of the 2nd ace to 1
def reduce_ace(cards):
    ace = cards.index(11, -1)
    cards[ace] = 1
    return cards

#Displays the final scoreline
def final_results(user_score, comp_score):
    if user_score > 21:
        print("\nYou busted. You lose this hand.")
    elif comp_score > 21:
        print("\nDealer busted. You win!")
    elif user_score == comp_score:
        print("\nIt's a push. Nothing won, nothing lost.")
    elif user_score == 21:
        print("\nBlackjack! You win!")
    elif user_score > comp_score:
        print(f"\n{user_score} is higher than {comp_score}, you win!")
    else:
        print(f"\n{user_score} is less than {comp_score}, you lose!")

print(logo)
game = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

while game == 'y':
    
    user_cards = deal_cards()
    comp_cards = deal_cards()
    user_score = sum(user_cards)
    comp_score = sum(comp_cards)

    #Loop for user when deciding whether to hit or stand. Automatically breaks if blackjack is achieved
    while True:
        print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {comp_cards[0]}")
        if user_score >= 21:
            break
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                user_cards.append(random.choice(deck))
                user_score = sum(user_cards)
            else:
                break

    #Loop for dealer to draw cards until reaching a value of at least 17
    while comp_score < 17:
        comp_cards.append(random.choice(deck))
        comp_score = sum(comp_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}\nComputer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
    final_results(user_score, comp_score)

    game = input("Do you want to play another game of blackjack? Type 'y' or 'n': ")
    os.system('cls')

print('Thanks for playing! Come back soon!')