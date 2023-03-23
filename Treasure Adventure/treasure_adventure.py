print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" \n").lower()
if direction == 'left':
    direction2 = input("You arrive at a flowing river. Do you try to swim across? Type swim or wait \n").lower()
    if direction2 == 'wait':
        direction3 = input("Eventually a river cruise boat floats by and picks you up.\nWhile exploring you find 3 colored doors. Do you open one of them? Type red, blue, yellow, or no \n").lower()
        if direction3 == 'red':
            print('You become engulfed in flames due to an engine malfunction. Game over.')
        elif direction3 == 'blue':
            print('As you open the door, 2 tigers emerge and eat you alive. Game over.')
        elif direction3 == 'yellow':
            print('You find a 5 star bedroom with a chest containing a ruby. You win!')
        else:
            print('Walking back to the deck, you suddenly felt motion sickness. As you leaned over to throw up, you accidentally went over board and drowned. Game over.')
    else:
        print('You were eaten by a trout of all things. Game over')
else:
    print('You fell into a hole and died a miserable death. Game Over.')