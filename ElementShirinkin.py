class ElementShirinkin():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
        
    @property
    def name(self):
        return self.__name
    
    @property
    def symbol(self):
        return self.__symbol
    
    @property
    def number(self):
        return self.__number
    
    def dump(self):
        print(f"Название элемента: {self.name}, символ: {self.symbol}, порядковый номер: {self.number}.")
        
this_element = ElementShirinkin('Cobaltum', 'Co', '27')

this_element.dump()
