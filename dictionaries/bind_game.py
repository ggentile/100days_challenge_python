import os

clear = lambda: os.system('cls')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
end_game = True
bid_game = {}

def find_highest_bid(bid_record):
    highest_bid = 0
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount 
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo)

print("Welcome to the secret auction program.")

while end_game == True:

    name = input("What's your name? ")

    bid = int(input("What's your bid? "))


    bid_game[name] = bid

    game_on = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if game_on == 'no':
        end_game = False
        find_highest_bid(bid_game)
    else:
        clear()
        print(bid_game)

    