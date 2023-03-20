#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Based on number of letters, symbols, and numbers, creates a list that is shuffled to finialize the password
pass_list = []
for n in range(1, nr_letters + 1):
  r_letter = random.choice(letters)
  pass_list.append(r_letter)
for n in range(1, nr_symbols + 1):
  r_symbol = random.choice(symbols)
  pass_list.append(r_symbol)
for n in range(1, nr_numbers + 1):
  r_number = random.choice(numbers)
  pass_list.append(r_number)
random.shuffle(pass_list)

password = ''
for n in pass_list:
  password += n
print(f"Here is your brand new password: {password}")