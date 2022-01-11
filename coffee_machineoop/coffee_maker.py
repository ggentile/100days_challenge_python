from data import MENU as menu
from data import resources as resources

class Coffee_maker:


    ingredientes = ["water", "milk", "coffee"]

    def __init__(self, options):
        self.isOn = True
        self.options = options


    def ligar_desligar(self, on):
        if on == True:
            on = False
            return on

    def check_resources(self):
        return resources
        
    def faz_cafe(self, option):
        index = 0
        user = list(menu[option]['ingredients'].values())
        available = list(resources.values())
        for ingredient in user:
            if ingredient <= available[index]:
                new_ingredients = available[index] -  ingredient
                up_dict = {Coffee_maker.ingredientes[index]: new_ingredients}
                resources.update(up_dict)
            else:
                print(f"I'm sorry, we don't have enough {ingredient}") 
                return False
            index += 1
        return True


