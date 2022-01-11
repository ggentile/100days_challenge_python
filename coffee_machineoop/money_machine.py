from data import MENU as menu


class Money:

    coins = {"quarters": 0.25,
                "dimes": 0.10, 
              "nickles": 0.05, 
              "pennies": 0.001}



    def __init__(self, option):
        self.option = option

    def recebe_dinheiro(self, option):
        print('Please, insert some coins.')
        quartes = float(input(f'How many quarters?')) * 0.25
        dimes = float(input(f'How many dimes? ')) * 0.10
        pennies = float(input(f'How many pennies? ')) * 0.05
        nickles = float(input(f'How many nickles? ')) * 0.001
        total = quartes + dimes + pennies + nickles
        if total > menu[option]["cost"]:
            change = round(total - menu[option]["cost"], 2)
            print(f"Here's your ${change} in change.")
            print(f'Here is your {option}. Enjoy!')
        elif total == menu[option]["cost"]:
            print(f'Here is your {option}. Enjoy!')
        else:
            print("Sorry, that's not enough money!")