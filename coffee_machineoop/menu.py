class Order:

    REPORT = 'report'
    options_available = ['espresso', 'latte', 'cappuccino', 'power']


    def __init__(self, option):
        self.option = option

    def recebe_ordem(self, ordem):
        self.ordem = ordem
        if self.ordem in Order.options_available or self.ordem == Order.REPORT:
            return self.ordem
        else:
            raise Exception('Error processing')

