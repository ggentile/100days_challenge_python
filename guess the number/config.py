import random

numbers = []
number_of_chances = ''


def computer_number():
    for x in range(1,101):
        numbers.append(x)
    return numbers


def game(mode):
    global number_not_found
    global number_of_chances 
    if mode == 'easy':
        number_of_chances = 10
    else:
        number_of_chances = 5
    computer = computer_number()
    num = random.choice(computer)
    while number_of_chances > 0:
        print(f"you have {number_of_chances} remaining to guess the number.")
        person_guess = int(input('Make a guess: '))
        if person_guess > num:
            print('Too high.\nGuess again.')
        elif person_guess < num:
            print('Too low.\nGuess again')
        else: 
            print(f'you got it! The answer was {num}.')
            exit()
        number_of_chances -= 1
    print("You've run out of guesses, you lose.")

    
