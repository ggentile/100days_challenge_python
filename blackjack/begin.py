from art import logo
from game import main


def menu():
    game_on = True
    while game_on == True:
        game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if game == 'n':
            print('all right! Take care.')
            game_on = False
        elif game == 'y': 
            print(logo)
            main()
        else:
            print("Insert either a 'y' or a 'n'")


menu()