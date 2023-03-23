from cm_data import flavors, resources
import os

def enough_resources(recipe):
    for item in recipe:
        if recipe[item] > resources[item]:
            print(f"Not enough {item} to complete the order")
            return False
    return True

def coins_inserted():
    print('Please insert coins')
    coins = int(input('How many quarters?: ')) * .25
    coins += int(input('How many dimes?: ')) * .1
    coins += int(input('How many nickels?: ')) * .05
    coins += int(input('How many pennies?: ')) * .01
    return coins

def enough_money(money):
    if money < drink['price']:
        print('Not enough money. Your purchase has been refunded')
        return False
    elif money > drink['price']:
        print(f"Here is ${(money - drink['price']):.2f} in change")
    resources['revenue'] += drink['price']
    return True

def dispense_drink(recipe):
    resources['water'] -= ingredients['water']
    resources['coffee'] -= ingredients['coffee']
    resources['milk'] -= ingredients['milk']
    print(f"Here is your {coffee}. Enjoy!")

while True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    os.system('cls')

    if coffee == 'off':
        break
    elif coffee == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: ${(resources['revenue']):.2f}")
        continue

    drink = flavors[coffee]
    ingredients = drink['Ingredients']
    if enough_resources(ingredients):   
        user_coins = coins_inserted()
        if enough_money(user_coins):
            dispense_drink(ingredients)