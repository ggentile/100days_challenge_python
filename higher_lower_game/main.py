from game_data import data
from art import logo, vs
import random
import os

clearConsole = lambda: os.system('cls')

def select_data():
    person = random.choice(data)
    return person


def more_followers(person_a, person_b):
    if person_a['follower_count'] > person_b['follower_count']:
        return 'a'
    else:
        return 'b'

def main():
    correct = True
    score = 0

    a = select_data()

    while correct == True:
        b = select_data()

        if a['name'] == b['name']:
            b = select_data()
         

        print(logo)

        if score != 0:
            print(f"You're right! Current score: {score}")

        print(f"Compare A: {a['name']}, a(n) {a['description']}, from {a['country']}")

        print(vs)

        print(f"Against B: {b['name']}, a(n) {b['description']}, from {b['country']}")


        guess = input('Who has more followers? Type A or B: ').lower()

        real_result = more_followers(a, b)

        if guess == real_result:
            score += 1
            a = b
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            correct = False


main()





