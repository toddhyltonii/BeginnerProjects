import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

symbols = [rock, paper, scissors]

try:
    choice = int(input('Rock, Paper, Scissors, Shoot! Type 0 for Rock, 1 for Paper, 2 for Scissors. '))
    print('You chose: \n' + symbols[choice])
except:
    print('\nYou typed an invalid number. You lose by default.')
    quit()

comp_choice = random.randint(0,2)
print('Computer chooses: \n' + symbols[comp_choice])

if (choice == 0 and comp_choice == 2) or (choice == 1 and comp_choice == 0) or (choice == 2 and comp_choice == 1):
  print('You win!')
elif choice == comp_choice:
  print('It is a draw!')
else:
  print('You lose!')
