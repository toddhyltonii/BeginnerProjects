print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? '))
percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

#Calulates price each person in the group should pay based on the bill
your_share = bill / people
tip = your_share * (percentage / 100)
total = (round(your_share + tip, 2))
print(f"Each person should pay: ${total:.2f}")
