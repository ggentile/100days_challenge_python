import random
from hangmanart import stages, logo
from words import word_list

game_end = False
computer_choice = random.choice(word_list)
len_computer_choice = len(computer_choice)
lives = 6

display = []

print(computer_choice)

for let in range(len_computer_choice):
    let = "_"
    display.append(let)


print(logo)

while not game_end:

    user_choice = input('Escolha uma letra: ').lower()

    for position in range(len_computer_choice):
        letter = computer_choice[position]
        if letter == user_choice:
            display[position] = user_choice

    print(display)

    if user_choice not in computer_choice:
        print(f"You guessed {user_choice}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_end = True
            print('You killed the hangman')

    if "_" not in display:
        game_end = True
        print('Congrats, you won the game')

    print(stages[lives])
