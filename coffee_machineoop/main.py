from money_machine import *
from menu import *
from coffee_maker import *


def main():
    machine_on = True
    while machine_on == True:
        ord = input('What would you like? (espresso/latte/cappucino): ').lower()
        ordem = Order(ord)
        answer = ordem.recebe_ordem(ord)
        maquina_check = Coffee_maker(answer)
        if answer == 'report':
            repo = maquina_check.check_resources()
            print(repo)
        elif answer != 'report' and answer != 'power':
            cobranca = maquina_check.faz_cafe(answer)
            if cobranca == True:
                charge = Money(answer)
                charge.recebe_dinheiro(answer)
            else:
                desligar = maquina_check.ligar_desligar(machine_on)
                machine_on = desligar
        else: 
            desligar = maquina_check.ligar_desligar(machine_on)
            machine_on = desligar


if __name__ == '__main__':
    main()
