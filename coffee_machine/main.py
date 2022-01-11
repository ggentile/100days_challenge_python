from data import resources, MENU


options_available = ['espresso', 'latte', 'cappuccino', 'REPORT']
coins = {"quarters": 0.25,
         "dimes": 0.10, 
         "nickles": 0.05, 
         "pennies": 0.001}

machine_on = True


REPORT = 'report'


def order():
    if user_preference in options_available:
        print('Please, insert some coins.')
        quartes = int(input(f'How many quarters?'))
        dimes = int(input(f'How many dimes? '))
        nickles = int(input(f'How many nickles? '))
        pennies = int(input(f'How many pennies? '))
        price = sum_money(quartes, dimes, nickles, pennies)
        if price >= MENU[user_preference]["cost"]:
            change = price - MENU[user_preference]["cost"]
            total_change = round(change, 2)
            print(f"Here's your ${change} in change.")
            print(f'Here is your {user_preference}. Enjoy!')
        else:
            print("Sorry, that's not enough money!")


def sum_money(quartes, dimes, nickles, pennies):
    val1 = float(coins.get('quarters')) * quartes
    val2 = float(coins.get('dimes')) * dimes
    val3 = float(coins.get('nickles')) * nickles
    val4 = float(coins.get('pennies')) * pennies
    total = val1 + val2 + val3 + val4
    x = round(total, 2)
    return x

def check_resources(drink_selected):
    index = 0
    resources_ingredients = ['water', 'milk', 'coffe']
    user = list(MENU[drink_selected]['ingredients'].values())
    available = list(resources.values())
    for ingredient in user:
        if ingredient <= available[index]:
            new_ingredients = available[index] -  ingredient
            up_dict = {resources_ingredients[index]: new_ingredients}
            resources.update(up_dict)
        else:
            print(f"I'm sorry, we don't have enough {resources_ingredients[index]}") 
            exit()
        index += 1


while machine_on == True:
    user_preference = input('What would you like? (espresso/latte/cappucino): ').lower()

    if user_preference in options_available:
        check_resources(user_preference)
        order()
    elif user_preference == REPORT:
        print(resources)#dict_values[]
    elif user_preference == 'power':
        machine_on = False
    else: 
        print('Error processing')
        machine_on = False


