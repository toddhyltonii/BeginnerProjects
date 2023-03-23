from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Encrypts/Decrypts message by shifting the letters down/up the alphabet
def caesar(user_dir, user_text, user_shift):
    message = ''
    for letter in user_text:
        if letter.isalpha() == True:
            alpha_index = alphabet.index(letter)
            if user_dir == 'encode':
                new_index = alpha_index + user_shift
                while new_index > 25:
                    new_index = new_index - 26
            elif user_dir == 'decode':
                new_index = alpha_index - user_shift
                while new_index < 0:
                    new_index = new_index + 26
            message += alphabet[new_index]
        else:
            message += letter
    print(f"\nThe {user_dir}d result is: {message}\n")

print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

#Calls caesar function using the user's input
    caesar(direction, text, shift)
    another_message = input('Do you need to encrypt/decipher another message? Type yes or no.\n').lower()
    if another_message == 'no':
        break

print('\nThank you for using the Caesar Cipher!')

