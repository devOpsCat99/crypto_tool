from objects.action import Action
class Buy(Action):

    # Constructor
    def __init__(self, buyPrice, money):
        self.__buyPrice = buyPrice
        self.__Money = money
    
    # Getters
    def getBuyPrice(self):
        return self.__buyPrice
    
    def getMoney(self):
        return self.__Money
    
    # Public Methods
    def execute(self):
        return self.__Money / self.__buyPrice
    
    # Print
    def __str__(self):
        return "Buy Price: " + str(self.__buyPrice) + " Money: " + str(self.__Money)
    