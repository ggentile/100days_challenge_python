from os import X_OK, error
import os
import operations as op

clear = lambda: os.system('cls')

resultado = '' 
validator = ''
end_calculator = False
operands = ['+', '-', '*', '/']

while end_calculator == False:
    if validator == '':
        num_1 = int(input("What's the first number? "))
    for operand in operands:
        print(operand)

    operation = input('Pick the operator: ')
    if operation not in operands:
        error('Select a valid operator')
    num_2 = int(input("What's the next number? "))

    if operation == '+':
        answer = op.soma(num_1, num_2)
        print(f'{num_1} {operation} {num_2} = {answer}')
    elif operation == '-':
        answer = op.subtrair(num_1, num_2)
        print(f'{num_1} {operation} {num_2} = {answer}')
    elif operation == '*':
        answer = op.multiplicar(num_1, num_2)
        print(f'{num_1} {operation} {num_2} = {answer}')
    else:
        answer = op.dividir(num_1, num_2)
        print(f'{num_1} {operation} {num_2} = {answer}')

    game_on = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or Even, type exit to exit: ").lower()

    if game_on == 'exit':
        print('See ya :)')
        end_calculator = True
    elif game_on == 'y':
        validator = X_OK
        num_1 = answer
    else: 
        validator = ''
        clear()

