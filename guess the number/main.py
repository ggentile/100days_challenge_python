import config as guess
from art import logo

game_on = True

print(logo)
print("Welcome to the Number Guessing Game!")

def main():
    while game_on == True:
        print("I'm thinking of a number between 1 and 100.")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'easy' or 'hard':
            guess.game(difficulty)
        else: 
            print('Please, seelct one of the options')
    


if __name__ == '__main__':
    main()