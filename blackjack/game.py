import random


cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def main():
    continua = True
    human = distribute_cards()
    computer = distribute_cards()
    print(f"Your cards: {human}")
    print(f"Computer's first card: {computer[0]}")
    while continua == True:
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == 'y':
            add_card(human)
            if sum(human) > 21:
                print('The computer won!')
                exit()
        elif choice == 'n':
            end_game(human, computer)
            continua = False
        else: 
            print('Just get real and decide if you really wanna play')
            exit()

def distribute_cards():
    """Return a random card from the deck"""
    value = []
    for _ in range(0, 2):
        value.append(random.choice(cards))
    return value


def end_game(list_player, list_computer):
    game = 21
    player = sum(list_player)
    machine = sum(list_computer)
    while machine < 17:
        add_card(list_computer)
        machine = sum(list_computer)
    print(f"Your final hand: {list_player}")
    print(f"Computer's final hand: {list_computer}")
    if player == game or player > machine or machine > 21:
        print('You won!')
    elif machine == game:
        print('The computer won')
    elif machine > player:
       print('The computer won') 
    else:
       print("It's a draw!") 


def add_card(some_list):
    some_list.append(random.choice(cards))
    return some_list




