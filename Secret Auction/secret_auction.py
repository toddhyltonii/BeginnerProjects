import os
from gavel import logo
all_bids = {}

#Determines which person bid the highest given a dictionary
def highest_bidder(bids):
    highest_bid = 0
    winner = ''
    for person in bids:
        if bids[person] > highest_bid:
            highest_bid = bids[person]
            winner = person
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

print(logo,'\n')
print('Welcome to the secret aution program.\n')
while True:

    try:
        name = input('What is your name?: ')
        bid = int(input('What is your bid?: $'))
    except:
        os.system('cls')
        print('Invalid bid amount. Retry entering your information.')
        continue

    all_bids[name] = bid
    another_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system('cls')
    if another_bid == 'no':
        break
    elif another_bid == 'yes':
        continue
    else:
        print('Invalid entry; therefore, no more bidders.\n')
        break
    
highest_bidder(all_bids)