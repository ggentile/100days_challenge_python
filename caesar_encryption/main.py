from art import logo
from function import caesar

answer = True
print(logo)

while answer == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    game = input("Type 'yes' if you wantt to go again. Otherwise type 'no'\n")

    if game == 'no':
        answer = False



